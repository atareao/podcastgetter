#!/usr/bin/env python3

import requests
import feedparser
import sqlite3
import os
import re
import sys
import csv
import base64
from dateutil.parser import parse
from PIL import Image

FORMAT_DESCRIPTOR = "#EXTM3U"
RECORD_MARKER = "#EXTINF"

PODCASTS = [
    'http://www.ivoox.com/salmorejo-geek_fg_f1206500_filtro_1.xml',
    'http://www.ivoox.com/podcast-linux_fg_f1297890_filtro_1.xml',
    'http://feeds.feedburner.com/ugeek',
    'https://www.eduardocollado.com/category/podcast/feed/',
    'https://compilando.audio/index.php/feed/podcast/',
    'https://www.ivoox.com/mosqueteroweb-tecnologia-linux-ajedrez_fg_f1248962_filtro_1.xml']


STYLE = '''.%s{\n\tbackground: url(\'data:image/png;base64,%s\');
\n\tbackground-size: 48px 48px;\n}\n'''


HTML = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta content="text/html; charset=utf-8" http-equiv="Content-Type">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0">
    <script type="text/javascript" src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>

    <script type="text/javascript" >
    var audio;
    var playlist;
    var tracks;
    var current;
    var previous;
    var current_track;
    var previous_track;
    var ntracks;
    function initaudio(){
        audio=$("audio");
        playlist=$("#playlist");
        ntracks=$("[id^=item-]").length
        audio[0].volume=1;
        current=0;
        previous=ntracks-1;
        current_track=playlist.find("#item-0");
        previous_track=playlist.find("#item-"+previous);
        runaudio(current_track, audio[0],false);
        $("#panelplayer").height("50px");
        $("[id^=item-]").click(function(e){
            e.preventDefault();
            previous=current;
            previous_track=current_track;
            remove_play(previous_track);
            current_track=$(this);
            current=current_track.parent().index();
            runaudio(current_track, audio[0]);
        });
        audio[0].addEventListener("ended",function(e){
            playnext();
        });
        audio[0].addEventListener("pause",function(e){
            $("#playing").hide();
            $("#panelplayer").height("50px");
        });
        audio[0].addEventListener("play",function(e){
            $("#playing").show();
            $("#panelplayer").height("auto");
        });
    };
    function playnext(){
        previous=current;
        previous_track=current_track;
        remove_play(previous_track);
        current++;
        current_track=playlist.find("#item-"+current);
        if(current_track.length==0){
            current=0;
            current_track=playlist.find("#item-0");
        }
        runaudio($(current_track),audio[0]);
    }
    function playprevious(){
        previous=current;
        previous_track=current_track;
        remove_play(previous_track);
        current--;
        current_track=playlist.find("#item-"+current);
        if(current<0){
            current=ntracks-1;
        }
        current_track=playlist.find("#item-"+current);
        runaudio($(current_track),audio[0]);
    }
    function remove_play(item){
        isp=$(item.find(".isplaying"));
        isp.html("");
    }
    function runaudio(item, player,play=true){
        isp=$(item.find(".isplaying"))
        isp.html("<i class='fa fa-play' aria-hidden='true'></i>");
        podcast=$(item.find(".podcast"));
        $("#podcast").text(podcast.text());
        track=$(item.find(".track"));
        $("#track").text(track.text());
        link=$(item.find('a'));
        player.src=link.attr("href");
        par=link.parent();
        par.addClass("active").siblings().removeClass("active");
        audio[0].load();
        if(play==true){
            console.log(play);
            audio[0].play();
        }
    }
    $(document).ready(function(){ 
        console.log($("[id^=item-]").length);
        $("#right").bind("click", function(e) {
            playnext();
        });
        $("#left").bind("click", function(e) {
            playprevious();
        });
        $("#playing").hide();
        initaudio();
    });
    </script>
    <link href="https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css?family=Roboto" rel="stylesheet">
    <style>
        #left{
            margin-top: 7px;
            float: left;
            width: 16px;
            height: 32px;
            cursor:hand;
        }
        #right{
            margin-top: 7px;
            float:left;
            width: 16px;
            height: 32px;
            cursor:hand;
        }
        $$STYLES$$
        body{
            background-color: rgb(247, 247, 247);
            font-family: "Roboto", sans-serif;
        }
        .panel{
            webkit-box-shadow: 0 0 1px rgba(0, 0, 0, 0.15);
            -moz-box-shadow: 0 0 1px rgba(0, 0, 0, 0.15);
            box-shadow: 0 0 1px rgba(0, 0, 0, 0.15);
            box-sizing: border-box;
            display: block;
            background-color: #fff;
            padding: 10px;
            margin: 0 auto;
            margin-bottom: 20px;
        }
        audio {
            width:250px; /* Ancho del reproductor */
            display: block;
            float:left;
        }
        ul {
          list-style-type: none;
          padding-left: 0px;
        }
        li {
            list-style-type: none;
            height:60px;
        }
        span[id^="item-"]{
            height:48px;
            line-height: 20px;
            display: block;
        }
        .isplaying{
            float:left;
            margin-top:12px;
            width:24px;
            height:24px;
            margin-right: 5px;
        }
        .logo{
            float:left;
            width:48px;
            height:48px;
            margin-right: 5px;
            background-size: 48px 48px;
            background-repeat: no-repeat;
        }
        .podcast, #podcast{
            display: block;
            font-size: 16px;
            font-weight: 400;
            color:rgba(0,0,0,.87);
        }
        .track, #track{
            display: block;
            font-size: 14px;
            font-weight: normal;
            color:rgba(0,0,0,.54);
            width: 200px;
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
        }
        #player{
            float:left;
        }
        .playingnow{
            font-size: 12px;
            color: #9E9E9E;
        }
        a{
            text-decoration:none;
            color:rgba(0,0,0,.54);
        }
        a:visited{
            text-decoration: none;
            color:rgba(0,0,0,.54);
        }
        @media only screen and (min-width: 700px) {
            .panel{
                width:600px;
            }
        }
        @media only screen and (max-width: 319px) {
            #player{
                float:none;
            }
            audio{
                width:120px;
            }
            .track,#track{
                width:150px;
            }
            .panel, #player{
                height: auto;
                min-height:50px;
            }
            #playing{
                display:inline-block;
            }
        }
        @media only screen and (min-width: 320px) and (max-width: 499px) {
            .track{
                width:70%;
            }
            #track{
                width:280px;
            }
            #playing{
                display:inline-block;
            }
        }
        @media only screen and (min-width: 500px) {
            .track{
                width:80%;
            }
            #track{
                width:35%;
            }
            #playing{
                display:block;
            }
        }
        @media only screen and (min-width: 600px) {
            #track{
                width:50%;
            }
        }
    </style>
</head>
<body>
    <div class="panel" id="panelplayer">
        <div id="player">
            <a href="#" id="left" onclick="return false" title="Anterior">
                <i class="fa fa-chevron-left" aria-hidden="true"></i>
            </a>
            <audio id="audio" preload="auto" tabindex="0" controls="">
                <source src="">
            </audio>
            <a href="#" id="right" onclick="return false" title="Siguiente">
                <i class="fa fa-chevron-right" aria-hidden="true"></i>
            </a>
        </div>
        <div id="playing">
            <span class="playingnow">Reproduciendo ahora...</span>
            <span id="podcast"></span>
            <span id="track"></span>
        </div>
    </div>
    <div class="panel">
        <ul id="playlist">
        $$PLAYLIST$$
        </ul>
    </div>
</body>
</html>
'''

DATABASE_FOLDER = os.path.join(os.path.expanduser('~'), '.config',
                               'podcastgetter')
DATABASE = os.path.join(DATABASE_FOLDER, 'podcastgetter.db')
M3U_FILE = os.path.join(DATABASE_FOLDER, 'podcasts.m3u')
MD_FILE = os.path.join(DATABASE_FOLDER, 'podcasts.md')
HTML_FILE = os.path.join(DATABASE_FOLDER, 'podcasts.html')


def normalize_class(class_name):
    return re.sub(r'\W+', '', class_name).lower()


class PodcastDB:
    def __init__(self):
        if not os.path.exists(DATABASE_FOLDER):
            os.makedirs(DATABASE_FOLDER)
        self.db = sqlite3.connect(DATABASE)
        cursor = self.db.cursor()
        cursor.execute('''
            CREATE TABLE if not exists podcasts(
            id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
            podcast_title TEXT NOT NULL,
            podcast_image_url TEXT NOT NULL,
            track_id  TEXT NOT NULL UNIQUE,
            track_date TEXT NOT NULL,
            track_title TEXT NOT NULL,
            track_url TEXT NOT NULL UNIQUE);
        ''')
        self.db.commit()

    def exists_entry_in_podcast(self, podcast, id):
        cursor = self.db.cursor()
        cursor.execute('''SELECT id FROM podcasts WHERE track_id=?''', (id,))
        return (cursor.fetchone() is not None)

    def add_entry(self, podcast_title, podcast_image_url, track_id, track_date,
                  track_title, track_url):
        print('=============')
        print(podcast_title, podcast_image_url, 'id:', track_id, 'url:',
              track_url)
        cursor = self.db.cursor()
        try:
            cursor.execute('''INSERT INTO podcasts(podcast_title, podcast_image_url,
track_id, track_date, track_title, track_url) VALUES(?, ?, ?, ?, ?, ?)''',
                           (podcast_title, podcast_image_url, track_id,
                            track_date, track_title, track_url))
        except sqlite3.IntegrityError as e:
            print('---', e, '---')
            return
        self.db.commit()

    def get_latest_podcast(self, podcast=None, limit=-1):
        cursor = self.db.cursor()
        if podcast is not None and limit > -1:
            cursor.execute('''SELECT podcast_title, track_title, track_url
 FROM podcasts WHERE podcast_title="{0}" ORDER BY track_date DESC LIMIT {1}'''.format(
            podcast, limit))
        elif podcast is not None and limit == -1:
            cursor.execute('''SELECT podcast, track_title, track_url
 FROM podcasts WHERE podcast="{0}" ORDER BY track_date DESC'''.format(podcast))
        elif podcast is None and limit > -1:
            cursor.execute('''SELECT podcast, track_title, track_url
 FROM podcasts ORDER BY track_date DESC LIMIT {0}'''.format(limit))
        else:
            cursor.execute('''SELECT podcast, track_title, track_url
 FROM podcasts ORDER BY track_date DESC''')
        return cursor.fetchall()

    def create_m3u(self):
        global STYLE
        global HTML
        cursor = self.db.cursor()
        cursor.execute('''SELECT podcast_title, podcast_image_url, track_title, track_url
 FROM podcasts ORDER BY track_date DESC''')
        rows = cursor.fetchall()
        md = []
        m3 = []
        mh = []
        styles = []
        podcast_classes = []
        for index, row in enumerate(rows):
            print('----', index, '----')
            podcast_title = row[0]
            podcast_class = normalize_class(podcast_title)
            podcast_image_url = row[1]
            track_title = row[2]
            track_url = row[3]
            md.append('{0} - [{1}]({2})\n'.format(row[0], row[2], row[3]))
            m3.append(RECORD_MARKER + ':-1,{0} - {1}\n'.format(row[0],
                                                               row[2]))
            m3.append('{0}\n'.format(row[3]))
            if podcast_class not in podcast_classes:
                styles.append(STYLE % (
                    podcast_class, create_base64(podcast_image_url)))
                podcast_classes.append(podcast_class)
            if index == 0:
                mh.append('<li class="active">\n')
            else:
                mh.append('<li>\n')
            mh.append('\t<span id="item-{0}">\n'.format(index))
            mh.append('\t\t<a href="{0}" title="{1}">\n'.format(
                track_url, track_title))
            mh.append('\t\t\t<span class="isplaying"></span>\n')
            mh.append('\t\t\t<span class="logo {0}"></span>\n'.format(
                podcast_class))
            mh.append('\t\t\t<span class="podcast">{0}</span>\n'.format(
                podcast_title))
            mh.append('\t\t\t<span class="track">{0}</span>\n'.format(
                track_title))
            mh.append('\t\t</a>\n')
            mh.append('\t</span>\n')
            mh.append('</li>\n')
        try:
            html = HTML.replace('$$STYLES$$', ''.join(styles) + '\n')
            html = html.replace('$$PLAYLIST$$', ''.join(mh) + '\n')
            fhtml = open('podcasts.html', 'w')
            fhtml.write(html)
            fmd = open('podcasts.md', 'w')
            fmd.write(''.join(md) + '\n')
            fp = open('podcasts.m3u', 'w')
            fp.write(FORMAT_DESCRIPTOR + '\n')
            fp.write(''.join(m3) + '\n')
        except Exception as e:
            print(e)
        finally:
            if fp:
                fp.close()
            if fmd:
                fmd.close()
            if fhtml:
                fhtml.close()

    def update_podcasts(self):
        for podcast in PODCASTS:
            print('----', podcast, '----')
            r = requests.get(podcast, verify=False)
            if r.status_code == 200:
                d = feedparser.parse(r.text)
                podcast_title = d.feed.title
                podcast_image_url = d.feed.image.url
                for entry in d.entries:
                    if not self.exists_entry_in_podcast(d.feed.title,
                                                        entry.id):
                        url = entry.enclosures[0]['url']
                        dt = parse(entry.published)
                        dt = dt.strftime('%Y%m%dT%H%M%S')
                        self.add_entry(podcast_title, podcast_image_url,
                                       entry.id, dt, entry.title, url)
                    print('=========================')
                    print(podcast_title)
                    print(podcast_image_url)
                    print(entry.id)
                    print(entry.title)
                    print(entry.published)
                    print(entry.enclosures[0])


def create_favorite_podcasts(csvfilename):
    global HTML
    global STYLE
    rows = []
    try:
        csvfile = open(csvfilename, 'r')
        csvreader = csv.reader(csvfile, delimiter='|')
        rows = list(csvreader)
        print(rows)
    except Exception as e:
        print(e)
    finally:
        if csvfile:
            csvfile.close()
    medium = []
    styles = []
    podcast_classes = []
    csvfile = open(csvfilename)
    csvreader = csv.reader(csvfile, delimiter='|')
    for index, row in enumerate(rows):
        print('---', index, '---')
        if len(row) == 3:
            feed, track_title, track_url = row
            r = requests.get(feed, timeout=5, verify=False)
            if r.status_code == 200:
                d = feedparser.parse(r.text)
                podcast_title = d.feed.title
                podcast_image_url = d.feed.image.url
                podcast_class = normalize_class(podcast_title)
                if podcast_class not in podcast_classes:
                    styles.append(STYLE % (
                        podcast_class, create_base64(podcast_image_url)))
                    podcast_classes.append(podcast_class)
                if index == 0:
                    medium.append('<li class="active">\n')
                else:
                    medium.append('<li>\n')
                medium.append('\t<span id="item-{0}">\n'.format(index))
                medium.append('\t\t<a href="{0}" title="{1}">\n'.format(
                    track_url, track_title))
                medium.append('\t\t\t<span class="isplaying"></span>\n')
                medium.append('\t\t\t<span class="logo {0}"></span>\n'.format(
                    podcast_class))
                medium.append('\t\t\t<span class="podcast">{0}</span>\n'.format(podcast_title))
                medium.append('\t\t\t<span class="track">{0}</span>\n'.format(
                    track_title))
                medium.append('\t\t</a>\n')
                medium.append('\t</span>\n')
                medium.append('</li>\n')
    html = HTML.replace('$$STYLES$$', ''.join(styles) + '\n')
    html = html.replace('$$PLAYLIST$$', ''.join(medium) + '\n')
    fhtml = open('podcasts_favoritos.html', 'w')
    fhtml.write(html)
    fhtml.close()


def create_base64(image_url):
    base64string = None
    print(image_url)
    temporal_old_image = image_url.split('/')[-1]
    temporal_new_image = 'temporal.png'
    if os.path.exists(temporal_old_image):
        os.remove(temporal_old_image)
    if os.path.exists(temporal_new_image):
        os.remove(temporal_new_image)
    try:
        r = requests.get(image_url, timeout=5, verify=False)
        if r.status_code == 200:
            with open(temporal_old_image, 'wb') as f:
                for chunk in r.iter_content(1024):
                    f.write(chunk)
            old_image = Image.open(temporal_old_image)
            old_image.thumbnail((48, 48), Image.ANTIALIAS)
            old_image.save(temporal_new_image, 'PNG')
            new_image_file = open(temporal_new_image, 'rb')
            base64string = base64.b64encode(new_image_file.read()).decode()
            new_image_file.close()
    except Exception as e:
        print(e)
    if os.path.exists(temporal_old_image):
        os.remove(temporal_old_image)
    if os.path.exists(temporal_new_image):
        os.remove(temporal_new_image)
    return base64string


if __name__ == '__main__':
    if len(sys.argv) > 1:
        create_favorite_podcasts(sys.argv[1])
    else:
        db = PodcastDB()
        db.update_podcasts()
        db.create_m3u()
    exit(0)
