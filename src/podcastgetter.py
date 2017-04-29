#!/usr/bin/env python3

import requests
import feedparser
import sqlite3
import os
from dateutil.parser import parse


FORMAT_DESCRIPTOR = "#EXTM3U"
RECORD_MARKER = "#EXTINF"

PODCASTS = [
    {'name': 'Salmorejo Geek',
     'url': 'http://www.ivoox.com/salmorejo-geek_fg_f1206500_filtro_1.xml'},
    {'name': 'Podcast Linux',
     'url': 'http://www.ivoox.com/podcast-linux_fg_f1297890_filtro_1.xml'},
    {'name': 'uGeek',
     'url': 'http://feeds.feedburner.com/ugeek'},
    {'name': 'Eduardo Collado',
     'url': 'https://www.eduardocollado.com/category/podcast/feed/'},
    {'name': 'Compilando Podcast',
     'url': 'https://compilando.audio/index.php/feed/podcast/'},
    {'name': 'MosqueteroWeb',
     'url': 'https://www.ivoox.com/mosqueteroweb-tecnologia-linux-ajedrez_fg_f1248962_filtro_1.xml'}]

DATABASE_FOLDER = os.path.join(os.path.expanduser('~'), '.config',
                               'podcastgetter')
DATABASE = os.path.join(DATABASE_FOLDER, 'podcastgetter.db')
M3U_FILE = os.path.join(DATABASE_FOLDER, 'podcasts.m3u')
MD_FILE = os.path.join(DATABASE_FOLDER, 'podcasts.md')
HTML_FILE = os.path.join(DATABASE_FOLDER, 'podcasts.html')


class PodcastDB:
    def __init__(self):
        if not os.path.exists(DATABASE_FOLDER):
            os.makedirs(DATABASE_FOLDER)
        self.db = sqlite3.connect(DATABASE)
        cursor = self.db.cursor()
        cursor.execute('''
            CREATE TABLE if not exists podcasts(
            id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
            podcast TEXT NOT NULL,
            entry_id  TEXT NOT NULL UNIQUE,
            entry_date TEXT NOT NULL,
            entry_title TEXT NOT NULL,
            entry_url TEXT NOT NULL UNIQUE);
        ''')
        self.db.commit()

    def exists_entry_in_podcast(self, podcast, id):
        cursor = self.db.cursor()
        cursor.execute('''SELECT id FROM podcasts WHERE entry_id=?''', (id,))
        return (cursor.fetchone() is not None)

    def add_entry(self, podcast, entry_id, entry_date, entry_title, entry_url):
        print('=============')
        print(podcast, 'id:', entry_id, 'url:', entry_url)
        cursor = self.db.cursor()
        cursor.execute('''INSERT INTO podcasts(podcast, entry_id, entry_date, entry_title, entry_url)
                          VALUES(?, ?, ?, ?, ?)''',
                       (podcast, entry_id, entry_date, entry_title, entry_url))
        self.db.commit()

    def get_latest_podcast(self, podcast=None, limit=-1):
        cursor = self.db.cursor()
        if podcast is not None and limit > -1:
            cursor.execute('''SELECT podcast, entry_title, entry_url
 FROM podcasts WHERE podcast="{0}" ORDER BY entry_date DESC LIMIT {1}'''.format(
            podcast, limit))
        elif podcast is not None and limit == -1:
            cursor.execute('''SELECT podcast, entry_title, entry_url
 FROM podcasts WHERE podcast="{0}" ORDER BY entry_date DESC'''.format(podcast))
        elif podcast is None and limit > -1:
            cursor.execute('''SELECT podcast, entry_title, entry_url
 FROM podcasts ORDER BY entry_date DESC LIMIT {0}'''.format(limit))
        else:
            cursor.execute('''SELECT podcast, entry_title, entry_url
 FROM podcasts ORDER BY entry_date DESC''')
        return cursor.fetchall()

    def create_md(self):
        latest = self.get_latest_podcast(limit=5)
        fmd = open(MD_FILE, 'w')
        fmd.write('#Podcast\n\n')
        fmd.write('##Ultimos podcasts\n')
        for podcast in latest:
            fmd.write('[{0} - {1}]({2})\n'.format(podcast[0],
                                                  podcast[1],
                                                  podcast[2]))
        for podcast in PODCASTS:
            latest = self.get_latest_podcast(podcast=podcast['name'])
            fmd.write('\n##{0}\n'.format(podcast['name']))
            for podcast in latest:
                fmd.write('[{0}]({1})\n'.format(podcast[1], podcast[2]))
        fmd.close()

    def create_m3u(self):
        cursor = self.db.cursor()
        cursor.execute('''SELECT podcast, entry_title, entry_url
 FROM podcasts ORDER BY entry_date DESC''')
        rows = cursor.fetchall()
        try:
            fhtml = open(HTML_FILE, 'w')
            fmd = open(MD_FILE, 'w') 
            fp = open(M3U_FILE, 'w')
            fp.write(FORMAT_DESCRIPTOR + '\n')
            fhtml.write('<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><title>HTML5 Audio Player</title><style>#playlist{list-style: none;}#playlist li a{color:black;text-decoration: none;}#playlist .current-song a{color:blue;}</style><!-- Source Code From YouTube.com/MicroTechTutorials  you may remove this message on your webpage but please do not redistribtue --></head><body><p>Demo Music From <a href="http://incompetech.com">incompetech.com</a></p><audio src="" controls id="audioPlayer">Sorry, your browser doesn\'t support html5!</audio><ul id="playlist">')
            for row in rows:
                fmd.write('{0} - [{1}]({2})\n'.format(row[0], row[1], row[2]))
                fp.write(RECORD_MARKER + ':-1,{0} - {1}\n'.format(row[0],
                                                                 row[1]))
                fp.write('{0}\n'.format(row[2]))
                fhtml.write('<li><a href="{2}">{0} - {1}</a></li>'.format(
                    row[0], row[1], row[2]))
        except Exception as e:
            print(e)
        finally:
            if fp:
                fp.close()
            if fmd:
                fmd.close()
            if fhtml:
                fhtml.close()

    def download_file(self, path, url):
        local_filename = url.split('/')[-1]
        filename = os.path.join(path, local_filename)
        # NOTE the stream=True parameter
        try:
            r = requests.get(url, stream=True)
            with open(filename, 'wb') as f:
                for chunk in r.iter_content(chunk_size=1024):
                    if chunk:
                        f.write(chunk)
                        # f.flush() commented by recommendation
            return True
        except Exception as e:
            print(e)
        return False

    def update_podcasts(self):
        for podcast in PODCASTS:
            r = requests.get(podcast['url'])
            if r.status_code == 200:
                d = feedparser.parse(r.text)
                print(d.feed.title)
                for entry in d.entries:
                    if not self.exists_entry_in_podcast(d.feed.title,
                                                        entry.id):
                        url = entry.enclosures[0]['url']
                        dt = parse(entry.published)
                        dt = dt.strftime('%Y%m%dT%H%M%S')
                        print(dt)
                        self.add_entry(podcast['name'], entry.id, dt,
                                       entry.title, url)
                    print('=========================')
                    print(entry.id)
                    print(entry.title)
                    print(entry.published)
                    print(entry.enclosures[0])



if __name__ == '__main__':
    db = PodcastDB()
    #db.update_podcasts()
    #db.create_m3u()
    print(db.get_latest_podcast())
    print(db.create_md())
    exit(0)

