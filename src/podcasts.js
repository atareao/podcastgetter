
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
    function setCookie(key, value){
      document.cookie = key + "=" + String(value);
    }
    function getCookie(key) {
        var b = document.cookie.match('(^|;)\s*' + key + '\s*=\s*([^;]+)');
        return b ? b.pop() : null;
    }
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
    function set_playingpanel_size(){
        var nw = ($("#panelplayer").width())-$("#player").width()-$("#controls").width();
        $("#playing").width(nw);
        var ps = parseInt($("#playing").width() - 75);
        $("#podcast").width(ps);
        $("#duration").width(75);
    }
    $(document).ready(function(){
        set_playingpanel_size();
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
            setCookie('podcast', this.value);
        });
        $("#search").click(function(e){
            if($("#inputbox").is(":visible")){
                $("#inputbox").hide();
            }else{
                if($("#for-speed").is(':visible')){
                    $("#for-speed").hide();
                }
                $("#inputbox").show();
                var left = $("span.control-icon.search-icon").position().left-$("#inputbox").width()+50;
                $("#inputbox").css("left", left);
                var top = $("span.control-icon.search-icon").position().top-$("#inputbox").height()-30;
                $("#inputbox").css("top", top);
            }
        });
        $("#speed").click(function(e){
            if($("#for-speed").is(":visible")){
                $("#for-speed").hide();
            }else{
                if($("#inputbox").is(':visible')){
                    $("#inputbox").hide();
                }
                $("#for-speed").show();
                $("#select-speed").val($("#speed-value").text().substring(0,3));
                var left = $("#speed-value").position().left-$("#for-speed").width()/2.0;
                $("#for-speed").css("left", left);
                var top = $("#speed-value").position().top-$("#for-speed").height()-30;
                $("#for-speed").css("top", top);
            }
        });
        $("#select-speed").change(function(e){
            speed = this.value;
            audio[0].playbackRate = speed;
            $("#speed-value").text(this.value+'x');
            setCookie('speed', this.value);
            $("#for-speed").hide();
        });
        $(window).resize(function(e){
            set_playingpanel_size();
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
        initaudio();
        var speedCookie = getCookie('speed');
        var podcastCookie = getCookie('podcast');
        if(speedCookie != null){
            speed = parseFloat(speedCookie);
            audio[0].playbackRate = speed;
            $("#speed-value").text(speedCookie+'x');

        }
        console.log(speedCookie, podcastCookie);
    });
