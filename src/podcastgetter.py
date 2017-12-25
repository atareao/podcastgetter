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
import io


FORMAT_DESCRIPTOR = "#EXTM3U"
RECORD_MARKER = "#EXTINF"

PODCASTS = [
    'http://www.ivoox.com/salmorejo-geek_fg_f1206500_filtro_1.xml',
    'http://www.ivoox.com/podcast-linux_fg_f1297890_filtro_1.xml',
    'https://www.ivoox.com/ubuntu-otras-hierbas_fg_f1412582_filtro_1.xml',
    'http://feeds.feedburner.com/ugeek',
    'https://www.eduardocollado.com/category/podcast/feed/',
    'https://compilando.audio/index.php/feed/podcast/',
    'https://www.ivoox.com/mosqueteroweb-tecnologia-linux-ajedrez_fg_f1248962_filtro_1.xml']


STYLE = '.%s{\tbackground: url(\'data:image/png;base64,%s\');}\n'


HTML = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    <title>uGeek – Podcast y Blog de Tecnología</title>
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0">
    <meta name="description" content="Podcast y Blog de Tecnología">
    <meta property="og:description" content="Podcast y Blog de Tecnología">
    <meta name="author" content="uGeek">
    <!--[if lt IE 9]>
      <script src="http://html5shiv.googlecode.com/svn/trunk/html5.js"></script>
    <![endif]-->
    <link rel="stylesheet" type="text/css" href="https://ugeek.github.io/style.css">
    <link rel="alternate" type="application/rss+xml" title="uGeek - Podcast y Blog de Tecnología" href="https://ugeek.github.io/feed.xml">
    <!-- Created with Jekyll Now - http://github.com/barryclark/jekyll-now -->

    <script type="text/javascript" src="https://code.jquery.com/jquery-3.2.1.min.js"></script>

    <script type="text/javascript">
    var audio;
    var playlist;
    var tracks;
    var current;
    var previous;
    var current_track;
    var previous_track;
    var ntracks;
    var position = 0;
    var speed = 1;
    class CookieManager{
        constructor(adocument){
            this.adocument = adocument;
            this.speed = this.readCookie('speed');
            this.podcast = this.readCookie('podcast');
            console.log(this.speed, this.podcast);
        }
        readCookie(name) {
              return decodeURIComponent(this.adocument.cookie.replace(new RegExp("(?:(?:^|.*;)\\s*" + name.replace(/[\-\.\+\*]/g, "\\$&") + "\\s*\\=\\s*([^;]*).*$)|^.*$"), "$1")) || null;
        }
        set_speed(speed){
            this.speed = speed;
        }
        get_speed(){
            return this.speed;
        }
        set_podcast(podcast){
            this.podcast = podcast;
        }
        get_podcast(){
            return this.podcast;
        }
        save(){
            var date = new Date();
            date.setTime(date.getTime() + (10*365*24*60*60*1000));
            var expires = "; expires=" + date.toUTCString();
            this.adocument.cookie = "speed=" + encodeURIComponent(this.speed) + expires + "; ";
            this.adocument.cookie = "podcast=" + encodeURIComponent(this.podcast) + expires + "; ";
        }
    };
    function next_random(){
        return Math.floor(Math.random()*ntracks);
    }
    function cpos(item){
        console.log(item);
        l = item.length;
        return parseInt(item.substring(5,l));
    }
    function format_time(seconds){
        var date = new Date(null);
        date.setSeconds(seconds); // specify value for SECONDS here
        return date.toISOString().substr(11, 8);
    }
    function initaudio(){
        audio=$("audio");
        playlist=$("#playlist");
        ntracks=$("[id^=item-]").length
        audio[0].volume=1;
        audio[0].addEventListener('timeupdate', function(){
            var duration = audio[0].duration;
            if(duration > 0){
                $("#duration").html(format_time(duration - audio[0].currentTime));
                position = 100 * (audio[0].currentTime / duration);
                $("#progressbar").val(position);
            }else{
                $("#progressbar").val(0);
            }
        });
        $("#progressbar").click(function(e){
            console.log(e.originalEvent.offsetX);
            console.log($("#progressbar").width());
            e.preventDefault();
            var duration = audio[0].duration;
            if(duration > 0){
                position = e.originalEvent.offsetX / $("#progressbar").width();
                audio[0].currentTime = duration * position;
            }
        });
        current=0;
        previous=ntracks-1;
        current_track=playlist.find("#item-0");
        previous_track=playlist.find("#item-"+previous);
        runaudio(current_track, audio[0],false);
        //$("#panelplayer").height("50px");
        $("[id^=item-]").click(function(e){
            e.preventDefault();
            current = cpos($(this)[0].id);
            if(previous == current) {
                if($("#play-pause .control-icon").hasClass('pause-icon')){
                    audio[0].pause();
                }else{
                    audio[0].play();
                }
            }else{
                previous=current;
                previous_track=current_track;
                remove_play(previous_track);
                current_track=$(this);
                current=current_track.parent().index();
                runaudio(current_track, audio[0]);
            }
        });
        audio[0].addEventListener("ended",function(e){
            playnext();
        });
        audio[0].addEventListener("pause",function(e){
            //$("#playing").show();
            //$("#panelplayer").height("50px");
            //$("#play-pause").html('<span class="control-icon play-icon" aria-hidden="true"></span>')
            $("#play-pause .control-icon").removeClass('pause-icon');
            $("#play-pause .control-icon").addClass('play-icon');
        });
        audio[0].addEventListener("play",function(e){
            //$("#playing").show();
            //$("#panelplayer").height("auto");
            //$("#play-pause").html('<span class="control-icon pause-icon" aria-hidden="true"></span>')
            $("#play-pause .control-icon").removeClass('play-icon');
            $("#play-pause .control-icon").addClass('pause-icon');
        });
    };
    function playpause(){
        if ($("#play-pause .control-icon").hasClass('play-icon')){
            audio[0].play();
        }else{
            audio[0].pause();
        }

    }
    function get_first_visible(){
        var all_tracks=$("[id^=item-]");
        var new_current = -1;
        for(var i=0; i<all_tracks.length; i++){
            if($(all_tracks[i]).parent().is(':visible')){
                new_current = i;
                break;
            }
        }
        if (new_current > -1){
            previous=current;
            previous_track=current_track;
            remove_play(previous_track);
            current = new_current
            current_track=playlist.find("#item-"+current);
            runaudio($(current_track),audio[0],!audio[0].paused);
        }
    }
    function playnext(){
        var all_tracks=$("[id^=item-]");
        var new_current = -1;
        for(var i=current+1; i<all_tracks.length; i++){
            if($(all_tracks[i]).parent().is(':visible')){
                new_current = i;
                break;
            }
        }
        if((new_current == -1) && (current > 0)){
            for(var i=0; i<current; i++){
                if($(all_tracks[i]).parent().is(':visible')){
                    new_current = i;
                    break;
                }
            }
        }
        if (new_current > -1){
            previous=current;
            previous_track=current_track;
            remove_play(previous_track);
            current = new_current
            current_track=playlist.find("#item-"+current);
            runaudio($(current_track),audio[0],!audio[0].paused);
        }
    }
    function playprevious(){
        var all_tracks=$("[id^=item-]");
        var new_previous = -1;
        for(var i=current-1; i >-1; i--){
            if($(all_tracks[i]).parent().is(':visible')){
                new_previous = i;
                break;
            }
        }
        if((new_previous == -1) && (current > 0)){
            for(var i=all_tracks.length - 1; i > current; i--){
                if($(all_tracks[i]).parent().is(':visible')){
                    new_previous = i;
                    break;
                }
            }
        }
        if (new_previous > -1){
            previous=current;
            previous_track=current_track;
            remove_play(previous_track);
            current = new_previous;
            current_track=playlist.find("#item-"+current);
            runaudio($(current_track),audio[0],!audio[0].paused);
        }

    }
    function download_audio(){
        console.log('aqui');
        var todownload = [];
        var elements = $("#playlist li input");
        for(var i=0; i < elements.length; i++){
            if($(elements[i]).is(':checked') == true){
                todownload.push($(elements[i]).parent());
            }
        }

        var link = document.createElement('a');
        link.setAttribute('download', null);
        link.style.display = 'none';
        document.body.appendChild(link);

        for(var i=0; i < todownload.length; i++){
            var url = $(todownload[i]).find('a').attr('href');
            var podcast = $(todownload[i]).find('span .podcast').text();
            var track = $(todownload[i]).find('span .track').text();
            console.log(url, podcast, track);

            link.setAttribute('href', url);
            link.click();
        }

        document.body.removeChild(link);

    }
    function remove_play(item){
        isp=$(item.find(".isplaying"));
        isp.html("");
    }
    function runaudio(item, player,play=true){
        isp=$(item.find(".isplaying"))
        isp.html('<span class="control-icon play-icon" aria-hidden="true"></span>');
        podcast=$(item.find(".podcast"));
        $("#podcast").text(podcast.text());
        track=$(item.find(".track"));
        $("#track").text(track.text());
        link=$(item.find('a'));
        player.src=link.data('media');
        par=link.parent();
        par.addClass("active").siblings().removeClass("active");
        audio[0].load();
        if(play==true){
            console.log(play);
            try{
                audio[0].play();
                audio[0].playbackRate = speed;
            }catch(e){}
        }
    }
    function volumemute(){
        var control = $("#volume .control-icon");
        if (control.hasClass('volume-icon')){
            control.removeClass('volume-icon');
            control.addClass('mute-icon');
            audio[0].muted = true;
        }else{
            control.removeClass('mute-icon');
            control.addClass('volume-icon');
            audio[0].muted = false;
        }
    }
    function randomnorandom(){
        var control = $("#random .control-icon");
        if (control.hasClass('random-icon')){
            control.removeClass('random-icon');
            control.addClass('norandom-icon');
            
        }else{
            control.removeClass('norandom-icon');
            control.addClass('random-icon');
        }
    }
    $(document).ready(function(){
        cookieManager = new CookieManager(document);
        $(document).keypress(function(e){
            if(!$("#inputbox").is(":visible")){
                console.log(e.originalEvent.key);
                switch(e.originalEvent.key){
                    case "s": // siguiente
                        playnext();
                        break;
                    case "a": // anterior
                        playprevious();
                        break;
                    case "p": //play/pause
                        playpause();
                        break;
                    case "m": // mute/volume
                        volumemute();
                        break;
                    case "r": //random / norandom
                        randomnorandom();
                        break;
                }
            }
        });
        $('#select-podcast').change(function(e){
            console.log(e);
            console.log(this.value);
            var elements = $("[id^=item-]");
            for(var i=0; i < elements.length; i++){
                var podcast = $(elements[i]).find(".podcast").text();
                if ((this.value == 'Todos') || (podcast == this.value)){
                    $(elements[i]).parent().show();
                }else{
                    $(elements[i]).parent().hide();
                }
            }
            get_first_visible();
            try{
                if(!audio[0].paused){
                    audio[0].pause();
                }
            }catch(e){}

            $("#inputbox").hide();
            cookieManager.set_podcast(this.value);
            cookieManager.save();
            console.log(cookieManager.get_podcast());
        });
        $("#search").click(function(e){
            if($("#inputbox").is(":visible")){
                $("#inputbox").hide();
            }else{
                $("#inputbox").show();
                //$("#inputbox").html("<input id='search-text' type='text' value=''>");
                var left = ($("#search").position().left - 200)+ "px";
                $("#inputbox").css("left", left);
                var top = ($("#search").position().top - 45) + "px";
                $("#inputbox").css("top", top);
                console.log(left);
                console.log(top);
            }
        });
        $("#speed").click(function(e){
            if($("#for-speed").is(":visible")){
                $("#for-speed").hide();
            }else{
                $("#for-speed").show();
                $("#select-speed").val($("#speed-value").text().substring(0,3));
                //$("#inputbox").html("<input id='search-text' type='text' value=''>");
                var left = ($("#search").position().left - 5)+ "px";
                $("#for-speed").css("left", left);
                var top = ($("#search").position().top - 35) + "px";
                $("#for-speed").css("top", top);
                console.log(left);
                console.log(top);
            }
        });
        $("#select-speed").change(function(e){
            speed = this.value;
            audio[0].playbackRate = speed;
            $("#speed-value").text(this.value+'x');
            cookieManager.set_speed(speed);
            cookieManager.save();
            $("#for-speed").hide();
        });
        $(document).click(function(e){
        });
        $("#right").bind("click", function(e) {
            playnext();
        });
        $("#left").bind("click", function(e) {
            playprevious();
        });
        $("#play-pause").bind("click", function(e){
            playpause();
        });
        $("#download").bind("click", function(e) {
            download_audio();
        });
        $("#volume").click(function(){
            volumemute();
        });
        $("#random").click(function(){
            randomnorandom();
        });
        $("#play-pause").html('<span class="control-icon play-icon" aria-hidden="true"></span>')
        initaudio();
    });
    </script>
    <style>
        body{
            background-color: rgb(247, 247, 247);
            font-family: "Roboto", sans-serif;
        }
        #speed-value{
            position: relative;
            top: 9px;
            line-height: 32px;
            font-size: 14px;
        }
        #select-podcast{
            width: 250px;
        }
        #for-speed,
        #inputbox {
            position: absolute;
            z-index: 1;
            background-color: rgba(255,255,255,.95);
            filter: drop-shadow(0 0 1px rgba(0, 0, 0, 0.15));
            //border-style: solid;
            //border-color: black;
            //border-width: 1px;
            border-radius: 5px;
            text-decoration: none;
            padding: 10px;
        }#for-speed:after,
        #inputbox:after {
            background: rgba(255,255,0,.95);
            border-radius: .5em;
            bottom: 0;
            color: #fff;
            display: block;
            left: 1em;
            padding: .3em 1em;
            position: absolute;
            text-shadow: 0 1px 0 #000;
            white-space: nowrap;
            z-index: 2;
        }
        #for-speed:before,
        #inputbox:before {
            border: solid;
            //box-shadow: -1px -1px 10px -2px rgba(0, 0, 0, 0.5);
            border-color: rgba(255,255,255,.95) transparent;
            border-width: 10px 10px 0 10px;
            bottom: -10px;
            content: "";
            display: block;
            left: 204px;
            position: absolute;
            z-index: 3;
        }
        #for-speed:before{
            left: 35px;
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
        #pocast, #track{
            padding:5px;
        }
        #player{
            line-height: 14px;
        }
        ul#playlist li input{
            position: relative;
            float: right;
            top: 10px;
        }
        #left, #right, #play-pause, #download{
            cursor:hand;
        }
        progress[value] {
          /* Reset the default appearance */
          -webkit-appearance: none;
           appearance: none;
          height: 10px;
          width: 100%;
        }
        progress[value]::-webkit-progress-bar {
            background-color: #ddd;
            border-radius: 5px;
            //box-shadow: 0 2px 5px rgba(0, 0, 0, 0.25) inset;
        }
        progress[value]::-webkit-progress-value {
            background-color: #888;
            border-radius: 5px;
            //box-shadow: 0 2px 5px rgba(0, 0, 0, 0.25) inset;
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
        .podcast, #podcast, #duration{
            font-size: 14px;
            line-height: 0.9;
            font-weight: 400;
            color:rgba(0,0,0,.87);
        }
        #podcast, #duration{
            display: inline-block;
        }
        #podcast{
            width: 85%;
        }
        #duration{
            width: 10%;
            text-align: right;
            margin-right: 10px;
        }
        .track, #track{
            display: block;
            font-size: 14px;
            font-weight: normal;
            color:rgba(0,0,0,.54);
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
        }
        span#track{
            width: 100%;
            margin: 0;
            margin-bottom: 5px;
            padding:0;
            line-height: 1;
        }
        #playing{
            float:left;
            width: 420px;
        }
        progress{
            display:block;
        }
        #player{
            float:left;
            height: 100%;
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
        #playing #podcast{
                white-space: nowrap;
                overflow: hidden;
                text-overflow: ellipsis;
        }
        @media only screen and (min-width: 700px) {
            .panel{
                width:600px;
            }
        }
        @media only screen and (max-width: 319px) {
            #left, #right{
                display: none;
            }
            #playing #podcast{
                width: 100px;
            }
            #playing{
                width: 170px;
            }
        }
        @media only screen and (min-width: 320px) and (max-width: 499px) {
            #playing #podcast{
                width: 70%;
            }
            #playing{
                width: 45%;
            }
        }
        @media only screen and (min-width: 500px) {
            #playing #podcast{
                width: 70%;
            }
            #playing{
                width: 60%;
            }
        }
        @media only screen and (min-width: 620px) {
            #playing #podcast{
                width: 80%;
            }
            #playing{
                width: 420px;
            }
        }
        .control-icon{
            position: relative;
            float: left;
            width: 32px;
            height: 32px;
        }
        #player .control-icon,
        #controls .control-icon{
            top: 9px;
        }
        .isplaying .play-icon{
            background-size: 24px;
            background-repeat: no-repeat;
        }
        .search-icon{background: url('data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAAN1wAADdcBQiibeAAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAMZSURBVFiF7ZbBaxxVHMc/v7dRmRQsUQ/VnrZUoWxbLx5UBimmQYjYeglF61/Qg4INM+up71KSCUsTiSjmD+glBbGWoqWVhRLMJWJT0kMPc21r2iLCZGe3zj4P3YWXyezMDrQHsd/Tb37v936/z7w3v/cGnun/LhkmSGutoiiaFJHjIvIu8BrwAnAH2AB+arfbywsLC389cYB6vX7UGHMOOFQQ+hA4G4bh18vLy8kTAfB9/wvgHKCGTWiM+bnT6Xwy7GpUcorXgUYG5KaI/A7cBgzwkj0oIvtHRkbertVq59fW1rpFACNZzt6yn00lXjfG1MMwvGIvsed5B4AzInLCCj8yNjY2C5wuAtixBVpr1Wq1/mD7nv/gOM6nWut4UCLP806JyDdWzkdKqYMzMzO38wB27G0URZN2cRFZ73Q6J/OKA8zNzX0LLFiu57rd7pd5czIBlFIf28/GmPr8/HyrKBGA4ziax93Q13Gtde4HnDX4jmVvhmF4ZZjiAFrrv4FLlmtPFEXVsgB7+4aI3CrT070569sKKLV3UOwggOf7hjGmU6Y4QLfbbadcTlmAO5adu3xZEpF9KaDNsgAblr2/1+dDqffBfWi52nEcbwyKzwQQkYsp15lhAba2tk4Cb1iuXxcXF9Nbkg8Qx/EFrFYSkROe550qKu77/iERWUy5vyuat+MuWF1djV3X/Qf4wIKYdF1398TExG/NZjP9RuL7/mfABWC3Ned6EARfFQFk3oZTU1OVarV6UUQmU0MPedznN4wxHRGpAh8Br2ekeQCMB0FwozQAgNb6xVar9SNwJC9BgQohBl7HzWazXavVzjuOswt4Ky+2LxG5DuwCRnuuUWDKdd1fVlZW7mXNyT2nl5aWHgVBcFopdRD4HribEdY2xlwGjs3Ozr4HHAXuW+MvA9d8338zEzoPIC2ttYrjeF+SJK8qpUZF5M8oim6lW61X7CrwiuV+kCTJ+41GY9tRXQqgjKanpw9XKpVrKYibQRActuOG/tcrq0ajsZ4kyThgH8V70nFPDaAPAYz3bsj7wOdPs94z/Tf1LxUBEIu9ILwxAAAAAElFTkSuQmCC')}
        .download-icon{background: url('data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAAN1wAADdcBQiibeAAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAH3SURBVFiF7ZW/a1NRFMc/9xm9jwwl0E51cXVKdQ6Iv7au4qL/QyDwfhBIHw0J3gdCl24dCk46d1NoKWQSFME9Yxdp1CUP8/qOS9QQnu9HYl2aLzy453B+fB6Xew6sdNWlFk1sNps127YVQBRFsre393WROtYiSZ7n7WutRyJyLiLnWuuR53n7/w0gSZJ6Ed+lAfxLrQBWALlzwHGcTcuyXoiIPeO+D2zMhX4Bjn8XViqyLMvt9/tnWfUrBSBvi8jzAnEbwJNfhoiQJMkhkAlwLa/qYDAYNhqNMfC4AMSsdowxh3lBuQBTiEFJiB1jzG6RwEIAJSEKNy8FUBCiVPPSADkQpZtDyitoNps1rfU9pdSNtITJZHJsjAkdx9FKqV0AEemEYdj1fX9dRB6k5YnID+DEGPMtE0BrfQLURSSduFL51Gq1HoVh2PU87wzAGHPg+/56kiTvgK2MH/4I3M0EAPLWar1Sqbxtt9vbvV7vAKDdbt+M4/gopznAnXlHkUGUpq04jj+7rnsEEMfxNlBbpNAyu6AGPJt+s81HItLhzwR8LyLmMgD+pg9hGHZF5HRqv6pWqx3ge1GAZEmAh67rDpVST6f2y/F4PATWgIsiAG+WBAC4NXO+DmxOz6/nA1PXcRAEa1EUlR5SWbJt+yIIgtRrWOlq6yfaU8H1tGrn/gAAAABJRU5ErkJggg==')}
        .mute-icon{background: url('data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAAN1wAADdcBQiibeAAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAL4SURBVFiF7ZfPSxRhGMe/zzu6KApBvzCRQAIlKFKCLllRVgZBQrLQoQj8B7q4r7O396LrO1iH6B52iraEkA6W6CGJ6NahSEGESGLpB3XQXdzeeTo4yjg7O05r7skvDMO87/PM9zMzz8zzDrCrKkoplVBKJfxjolrmUsr2fD6/UCgU5v0QVQGQUrYT0QyAFma2/HPbAkilUh22bXdGxaTT6TYimgZwCEBOCNGjlFrdNoCU8roQ4h0zvxkYGGgoZ+667gyAZs/8QiaT+eiPqanUnIgeA6gFUJtIJBoBLK/PK6XE6upqhzFmIsq8IoCAeagKhcI4M/d6h9/KmQP/+AjimKfT6TZmvugbYtd1rXLxsQHimnvPvAHAbwA/ARwEMCWlbAnLoRCjo0KIY4HhFmbW5cwty2pi5j3BgjPGGCKaAtAC4KXWuieYW3IHiGiWmZ8EtntRV26MOeIzBxF9KhaL3x3HmSOi2wAYwOXBwcGzWwIA2FvOKELPADQz8y8iMsx8zrKsiWQyaY2MjEwDeAUAzHwrDkAlagKQsyzrNDNfBbAC4FRra2svABBR1tt37RTAxqumtZ70GZ4BAGae9+IO7wiAEKLP/54zc0lxl839HwBEtH6FsG37CoCkB/Lam2/zpj/vCIDPvI+ZXwCoB/B2cXHxuQeyDjQbB+BHpQCu6xLWvi0TQohr2WzWSCm7AVwCACIaC+aU9AIhRBczHw8MdzKzjZAPl1+O4zxVSjUqpVaAjXXAmJc3qbUuuQNbFkugpYbKsqym4eHhnP+8UsqbRHQXwAEAuZqampNDQ0NLwdzIGgjp53cAFLeCtm37ARE98syXAHSHmUcClFlM3GfmGzEgGgD8AfBQCHFCa/2hXGAoQNRKxnGc8a0g6urq+uvr6/dprfszmUxkUZfUQJxlFLCpPRtjzP7R0dHlYEwcbQKIa76uVCrVIYRgrfX7Ssw3ASilEvl8fgFrvfsrM593HGeu0hPH1aYaICID4Eu1zEsU9uu0q53WX4YzcWSfcmYGAAAAAElFTkSuQmCC')}
        .next-icon{background: url('data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAAN1wAADdcBQiibeAAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAADrSURBVFiF7c4xDoIwGIbhr4WNO5i4ewaCg65ehqRrVxK4kDFGPIGDu5E7sLWNizFM8rf9CQN8G6Tt+wDrlj4xdkAp9TDGnJqmeVMeVEq1APLv56WqqsO/85Lw5i5N03tZltuxg1prOYgDwH7sDgUAAJskSW4UhO+ogMkQPoBJEL4AdkQIgBURCmBDxABYELGAaAQH4Ifo+94bwQUAgI2U8jwnIGicgM45d5wL0FlriyzLXnMAOmttUde1d5wDEBWPBUTHYwAs8VAAWzwEwBr3BbDHfQCTxKmApzEmp8S11k4I0Q5+XcNp65ayD6zqcjG5GpGBAAAAAElFTkSuQmCC')}
        .norandom-icon{background: url('data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAAN1wAADdcBQiibeAAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAADUSURBVFiFY2AYBaNggAEjrQyuqKgQ/P//fxUnJ2dlQ0PDH1zqmGjlgL9//4owMDCUfP/+fUVaWhor3R2ABIIFBQWX43IERhSUl5cvZGBgkKKCxVwMDAxWSPw1nJyckejRwYJFYxwVLMcGQr59+/aXgYEhAlmQHlGAF2ALgXUMDAx8VDAbIwq4uLhi0BXRLBuWlpaqMjEx3YJy175//z5y1qxZv9HV0SMKcFpOUwcwMzO/YWBg6OHk5IzAZfkoYGAYrQtG64LRumC0LhitC0bBKBgEAAAOAGhJoCzqggAAAABJRU5ErkJggg==')}
        .pause-icon{background: url('data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAAN1wAADdcBQiibeAAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAABUSURBVFiF7c6xDYAwDETRO9YC1soOngsPRk+Q3Fhp8n9p6awn0e75exhjpO2z2GVE3B27YxLVTyTp6tpNgNUBAAAAAAAAAAAAAPAHyGpk+2nc0ea9wQUOOLfT2RgAAAAASUVORK5CYII=')}
        .play-icon{background: url('data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAAN1wAADdcBQiibeAAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAFRSURBVFiF7davT8NAGMbx573DESwJyAkEAv6JOfQkEiyC5t5mggTB0nZTBIPAQFC1YGB/AYIfE4QAszBPkNcXdQOxwHZtV8G+srlrP+IRBWb992jUQ2a+AXCfZdleu90elAlQI1VEiwC2lFKvxpjIGLMwVcCP5omIiegpDMPtRqOhpw1wLYvIca1W6zHzRhUA1yqAC2a+Zub1KgCuOoDbMAxPm83mUhUAAFAismmtfckz1DwAV66hFgFweQ21SIBrONQgCNaqALjqWuu7v4ZaJgD4HuozM+9UARgmIlIFICOiM631SpIkh6MOzJX48a61drfT6fR+O1QG4BGAieP4cpzDRQLeiGi/3++fpGlqx71UBOBTRI4AHMRx/DHp5TyAjIjOlVLcarXefV/iC+gCCKIoevD9sC9gooEVCfAaWBGAXAPzBojIAMDVNH7LZ836AmeLkJG06jl7AAAAAElFTkSuQmCC')}
        .previous-icon{background: url('data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAAN1wAADdcBQiibeAAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAADuSURBVFiF7dQ9DoJAEAXgh5mWK2BibeEN/OFIFNNuQwLHsVfRM1hbeQmKjWtnrGSZfYkFvIpi2Pcl+wPMmXqyoQFVPQEoASDLslvTNLuYhauqWorIsW3bza+5RcRan8IQwtY5N/iPqhYicgGwHpqNAYyKqhYAOgCrmHkqYGw5FWAppwGs5RRASnkyILU8CcAoNwNY5SZA3/e0chMghHBmlZsA7IwGeO8PAB5/A+R5/hSRPQth2oK6rmkI8xlgIZIOIQORfAtSEZRrmIKgvQNWBPUhsiDoL+FYRAyg+/q+OudeMQjvfQngHoOYM+28AUNcWSpk+Oj8AAAAAElFTkSuQmCC');}
        .random-icon{background: url('data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAAN1wAADdcBQiibeAAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAKtSURBVFiF7ZbBS1RRFMZ/904z8oagJKFaCLUQAoNWtnBTgYv2WmhUS6PCheDMey+KHhTYe5lT2kooCCRbKC2CNkELwT+hjbQIqVaSBTGT2runRTN1e844Tmm18IMH9x2+e75vznn3noFtbOMfQ21VYs/zmkXkiuM4fhAEX2vx9FYZiOO4BRgqlUpP+vv703/dgIXu5ubmqVom1rTAdd1pYBeAUuoLsCAic8VicWZ8fHw5yfd9f48x5jRwFNgLVISyQKdFnXYcpy/Zjh3VHFcWIlJZXnIc55bv+33Dw8NzlWA+nz9njBkDdlf7dQn0FIvFGOi1gxtugVKq1Rjz0vO84wCu615QSj3aoHhNVKvAdCLpYWBfeZ0RkWv5fP4zMMavLXwLzAOm/L6mBdls9mxSrO4xDIIgUyqVRoHLAEqpEyISAR1ligBDYRgWymsAcrlcm9Z6viJerf9QvQJJAyvAgOu6bYCO43in1rrDotwPw3B0nRQ1xTdkoAzRWg8aY1q11let+Cel1PVqG1Kp1KKIjNS7iBq6CV3X7QR+nAIRuR1FUb6RHEk0ehHlrPVKOp2+9yfi0EAFfN8/ZIx5xU/TD0VkdnV19VmhUPiQ5G/2LFBxHBcsvtFa31FKXW9qarpRbYM1C6aCIKj5rdU1MDAw0OR53l2l1Ekr/FhEOoGDInLR87wctavZs56JerMgLSLtQItFWRSRI0qpOeCAFX8DvLbeNzQLqlWgG+gCukTkWEJ8WUTORFH0XkRuYl08ZTNd1mOLw/dZMJkUa+QULCilTkZR9AIgiqIHwHngYwM51qDeLFgWkXfAbDabfRoEQdEmhmE4OTg4+DyTyZwC2oH91t7NmQW/i8QsmFlaWuqbmJhYTfL+xj+imuJbaiCVSi0CI47j9NYS38Y2/gt8A/aGEunL3n3ZAAAAAElFTkSuQmCC')}
        .volume-icon{background: url('data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAAN1wAADdcBQiibeAAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAJYSURBVFiF7ZQ7aBRRFIa/c2cNuyZYaBSRIKRRBCURwSraBB+gKEQWLHyR3iq7d255mzxmiFa2Eh+NuBKQYBEMNgaRdBYW2gSEFEG0EM0GdPfYrLBMNslk8wBhfxgG5p57v4/LmQOttPI/p1gs9jrnTm7mDNPsRmvtgDFmTlXfFQqF9h0VsNYOiMgzYBeQbWtr66hf994b7/2ebRFIwBtmeXn5Ublc/h6G4cTQ0FDnlgmkgQOo6g8gAO5kMpkPYRie2LRAWjhAFEV3VfUW8BU4BMxYa7sa1WYagI4ZY44nPnepapQG7r3f7b1fiuP4qbV2TkRmgC4ReQhcSNavuAERmVXV54nnfhq4cy5fLpd/OuemCoXCgTiOP4nIbUCB82EYnl1XANi7Hmi1VKvVClBV1ctBEEzl8/lgbGzsDfAaQFVvphFoOnEcTwKXgCXgdHd391UAESnV3n3bKgAQRdF0HfAMgKp+ri0f3naBGlDS1m65gHPuIpCvibwFEJEjteUv2yrgnLumqq+AHPB+fn7+ZU3kn9BsGoFvzQpUq1UBBJgyxlwplUoVa20/cA5ARB4n96wYRMaYPlVNjs5UgyiO4xfe+w7v/RKAtfZoDSrAdBRFK24gdbOsNYqDIDg4MjKyWH+utfaGiNwD9gOLmUzm1PDw8EJyb+oeiON4UlWvA7/Xq3XOPRCRJzX4AtDfCL4hgQ1KtAN/gAljTE8URR9XK9zwX5BGIpvNDuZyuX1RFA2Ojo6u2dSpeyCZup6oVCqVzvHx8V/NntV0isVibxiGPTsObqWVrcxfG/nyu6kZSvIAAAAASUVORK5CYII=')}

        $$STYLES$$

    </style>
</head>

  <body>
    <div class="wrapper-masthead">
      <div class="container">
        <header class="masthead clearfix">
        <a href="/" class="site-avatar"><img src="https://avatars2.githubusercontent.com/u/27757712?v=3&amp;s=460"></a>
          <div class="site-info">
            <h1 class="site-name"><a href="#" data-media="https://ugeek.github.io/">uGeek</a></h1>
            <p class="site-description">Podcast y Blog de Tecnología</p>
          </div>

          <nav>
            <a href="#" data-media="https://ugeek.github.io/">Blog</a>
            <a href="#" data-media="https://ugeek.github.io/Temas">Temas</a>
    <a href="#" data-media="https://ugeek.github.io/search">Buscar</a>
          <a href="#" data-media="https://ugeek.github.io/podcasts">►Play</a>
        <a href="#" data-media="https://ugeek.github.io/about">Sobre mi</a>

          </nav>
        </header>
      </div>
    </div>

    <div id="main" role="main" class="container">
      <article class="page">

  <h1></h1>

  <div class="entry">

    <div id="inputbox" style="display: none;">$$SELECT$$</div>
    <div id="for-speed" style="display: none;">
        <select id="select-speed">
            <option value="0.8">0.8x</option>
            <option value="1.0">1.0x</option>
            <option value="1.2">1.2x</option>
            <option value="1.4">1.4x</option>
            <option value="1.6">1.6x</option>
            <option value="1.8">1.8x</option>
            <option value="2.0">2.0x</option>
        </select>
    </div>
    <div class="panel" id="panelplayer" style="height: 70px;">
        <div id="player">
            <a href="#" id="left" onclick="return false" title="Anterior">
                <span class="control-icon previous-icon" aria-hidden="true"></span>
            </a>
            <a href="#"id="play-pause" onclick="return false" title="Reproducir">
                <span class="control-icon play-icon" aria-hidden="true"></span>
            </a>
            <a href="#" id="right" onclick="return false" title="Siguiente">
                <span class="control-icon next-icon" aria-hidden="true"></span>
            </a>


            <audio id="audio" preload="auto" tabindex="0" src="http://www.ivoox.com/radiogeek-el-gobierno-argentina-aprobo-la_mf_22791929_feed_1.mp3">
                <source src="">
            </audio>
        </div>
        <div id="playing">
            <span id="podcast"></span>
            <span id="duration"></span>
            <span id="track"></span>
            <progress id="progressbar" max="100" value=""></progress>
        </div>
        <div id="controls" style="float: left;">
            <!--
            <a href="#" id="volume" onclick="return false" title="Volumen">
                <span class="control-icon volume-icon" aria-hidden="true"></span>
            </a>
            <a href="#" id="random" onclick="return false" title="Volumen">
                <span class="control-icon norandom-icon" aria-hidden="true"></span>
            </a>
            -->
            <a href="#" id="search" onclick="return false" title="Filtrar">
                <span class="control-icon search-icon" aria-hidden="true"></span>
            </a>
            <a href='#' id="speed" onclick="return false" title="Velocidad">
                <span id="speed-value" aria-hidden="true">1.0x</span>
            </a>
            <!--
            <a href="#" id="download" onclick="return false" title="Descargar">
                <span class="control-icon download-icon" aria-hidden="true"></span>
            </a>
            -->
        </div>
    </div>

    <div class="panel">
        <ul id="playlist">
            $$PLAYLIST$$
        </ul>
    </div>
  </div>
</article>
    </div>
    <div class="wrapper-footer">
      <div class="container">
        <footer class="footer">
          <!-- 
 -->

<p center>
    <a href="http://feeds.feedburner.com/ugeekblog">
        <img style="float: left;" src="https://ugeek.github.io/img/icon/podcast.png" alt="" width="30" height="30"/>
    </a>
    <img style="float: left;" src="https://ugeek.github.io/img/icon/transparente.png" alt="" width="20" height="20" />
    <a href="http://feeds.feedburner.com/ugeek"> <img style="float: left;" src="https://ugeek.github.io/img/icon/feed.png" alt="" width="30" height="30"/>
    </a>
    <img style="float: left;" src="https://ugeek.github.io/img/icon/transparente.png" alt="" width="20" height="20" />
    <a href="http://t.me/ugeek">
        <img style="float: left;" src="https://ugeek.github.io/img/icon/telegram.png" alt="" width="30" height="30" />
    </a>
    <img style="float: left;" src="https://ugeek.github.io/img/icon/transparente.png" alt="" width="20" height="20" />
    <a href="https://anchor.fm/ugeek">
        <img style="float: left;" src="https://ugeek.github.io/img/icon/anchor.png" alt="" width="30" height="30" />
    </a>
    <img style="float: left;" src="https://ugeek.github.io/img/icon/transparente.png" alt="" width="20" height="20" />
</p>
<p>
    <img style="float: right;" src="https://ugeek.github.io/img/icon/cc.png" alt="" height="30" />
</p>
<br>
</footer>
</div>
</div>

    
    <!-- Google Analytics -->
    <script>
        (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
        (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
        m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
        })(window,document,'script','https://www.google-analytics.com/analytics.js','ga');

        ga('create', 'UA-98100689-1', 'auto');
        ga('send', 'pageview', {
          'page': '/podcasts/',
          'title': ''
        });
    </script>
    <!-- End Google Analytics -->


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
        podcast_titles = []
        for index, row in enumerate(rows):
            print('----', index, '----')
            podcast_title = row[0]
            if podcast_title not in podcast_titles:
                podcast_titles.append(podcast_title)
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
            mh.append('\t\t<a href="#" data-media="{0}" title="{1}">\n'.format(
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
            sorted(podcast_titles)
            podcast_titles.insert(0, 'Todos')
            print(podcast_titles)
            selecthtml = ''
            selecthtml = '<select id="select-podcast">\n'
            for pt in podcast_titles:
                selecthtml += '\t<option value="{0}">{0}</option>\n'.format(pt)
            selecthtml += '</select>\n'
            html = HTML.replace('$$SELECT$$', selecthtml)
            html = html.replace('$$STYLES$$', ''.join(styles) + '\n')
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
    try:
        r = requests.get(image_url, timeout=5, verify=False)
        if r.status_code == 200:
            writer_file = io.BytesIO()
            for chunk in r.iter_content(1024):
                writer_file.write(chunk)
            old_image = Image.open(writer_file)
            old_image.thumbnail((48, 48), Image.ANTIALIAS)
            new_image = io.BytesIO()
            old_image.save(new_image, "png")
            base64string = base64.b64encode(new_image.getvalue())
    except Exception as e:
        print(e)
    if base64string is not None:
        return base64string.decode()
    return None


if __name__ == '__main__':
    if len(sys.argv) > 1:
        create_favorite_podcasts(sys.argv[1])
    else:
        db = PodcastDB()
        db.update_podcasts()
        db.create_m3u()
    exit(0)
