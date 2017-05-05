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

HTML_START = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>HTML5 Audio Player</title>
    <script type="text/javascript" src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>

    <script type="text/javascript" >
    var audio;
    var playlist;
    var tracks;
    var current;
    var ntracks;
    function initaudio(){
        audio=$("audio");
        playlist=$("#playlist");
        ntracks=$("[id^=item-]").length
        audio[0].volume=1;
        current_pista=playlist.find("#item-"+current);
        current=0;
        current_pista=playlist.find("#item-0");
        $("[id^=item-]").click(function(e){
            e.preventDefault();
            link=$(this);
            current=link.parent().index();
            runaudio(link, audio[0]);
        });
        audio[0].addEventListener("ended",function(e){
            playnext();
        });
        audio[0].addEventListener("pause",function(e){
            $("#playing").hide();
        });
        audio[0].addEventListener("play",function(e){
            $("#playing").show();
        });
    };
    function playnext(){
        current++;
        current_pista=playlist.find("#item-"+current);
        if(current_pista.length==0){
            current=0;
            current_pista=playlist.find("#item-0");
        }
        runaudio($(current_pista),audio[0]);
    }
    function playprevious(){
        current--;
        if(current<0){
            current=ntracks-1;
        }
        current_pista=playlist.find("#item-"+current);
        runaudio($(current_pista),audio[0]);
    }
    function runaudio(item,player){
        title=$(item.find(".title"));
        $("#podcaster").text(title.text());
        link=$(item.find("a"));
        episode = link.text()
        if(episode.length>33){
            $("#episode").text(link.text().substring(0,30)+"...");
        }else{
            $("#episode").text(link.text());
        }
        player.src=link.attr("href");
        par=link.parent();
        par.addClass("active").siblings().removeClass("active");
        audio[0].load();
        audio[0].play();
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
    <link href="https://fonts.googleapis.com/css?family=Roboto" rel="stylesheet">
    <style>
        #left{
            background: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAgCAYAAAAbifjMAAAAl0lEQVRIx+3UMQoCMRRF0aO1VloKdroM3YvgSsRdiJ2uwkYstRbciVVsZmAMMmYmbS6EVO9+Ql5CodCNMc549AkvcUGoVhKDal/j1QiHLpO3eEfhkDp9/yOYJJji2BJuFcxx+xNuFTwTwl+CYSQIuWWZ4ZpzBJjgkCOor3GXI6jZ9C1Ss8qrnCrXLPo8ppgRTriXn60Q8wECX1R63JgTcwAAAABJRU5ErkJggg==");
            float: left;
            width: 16px;
            height: 32px;
            cursor:hand;
        }
        #right{
            background: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAgCAYAAAAbifjMAAAAjUlEQVRIx+3UOwoCQRCE4W+NNdJQMNNj6F0ETyLeQsz0FJuIoaYG3mSjNtlgQRDtSaegkoH+KaYfVFV96o4zxllA9G6xLAEEXlj3700GEOiwzSYYev9rivjiI6YlgMAV8xJA4DksGCU61ZQkuGGRBZwwy37iIdvGDruSUd5kR7nFKrNMD1wwqZet6h+9AfPLU3sbivmUAAAAAElFTkSuQmCC");
            float:left;
            width: 16px;
            height: 32px;
            cursor:hand;
        }
        .compilandopodcast{
            background-image: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADAAAAAwCAMAAABg3Am1AAAAYFBMVEUREyMZGywnGS1HGi1BIEEsLz9/HjfqHTe7LkQ0VktMTloAcBB9R1b6KUJHWXo1ckbFUV5pbHT4R1v2WGoAsw/Mb3robXyFipGghpqorbD2nqb2ur3Mz9Dz19jn6OX4+fWMNKc4AAAAAWJLR0QAiAUdSAAAAAlwSFlzAAAN1wAADdcBQiibeAAAAAd0SU1FB+EFBQoqJLANsOoAAAJcSURBVEjHzZQBd6MgDIBRCzKsrIBCISD//18uUNe6XbW3d+/dXVoxJHwkAYE0PxTyNwGqPm2ECpTnk20Bv77dkqtEcQAIHHfz+3V4RRTZAahoXC4ALcMXJygVviCePAWILwzqAsd7QVBTShFVeoerVOZ3N1Upx89N/CUG2VZMMIvPrIVSQjgaH5ZvAE5M1CaDYZr8uY0UK6LPAF8qwIRQdb5UL05SymEYBIbYqwErxvD0lrbygimPbfxaxVbHjDA6pl3qFs5RJSV1WNce4HIs6dKas2CMKeeQq9M8BXyOD3iYBvdGhZQYV7wGYm6u3RrjEKD3+odJOu/VdXg/Au5LTijOT+UV984fARuX9PFtmiTn8RCI9750lJ2u0pXP8QB4+IY354fpXX4xPgHuVZQv43RSLr8A8rJaMP/ovcwvgbzU89PIU4dZ5UPARZR6+BFhJ1qHo2nZA0gRVe+A6CuKO1lsxxcZdfdLYxG/dfMRPAtFnCD/+m79IdC2bWlv77XTbl0bgF1mzvh8YRfOL/xSlQtrOtT4auItn2e+Au2cbNKLAbMAJJN00tlm3ZwXgw6w2Sw29MmGwFYgwNjr3INdgk3oXXQ2Bcg2BfzhHD2YbCx8AjMY0FmDTVaXCLpHwBiz9BCSMWiyYYRHhIZpM3JtdK/xNWreMWyNGXVv9M1kRsaNHrs/3Ye269oGn64ratHa2mv3gC6BMQA6AZ8hjAGshaAB+D5gbdAW1xigH3XC4Sb0wbB9YBwtlO0wNmAgjAa4orbbBThuL6/Cyp9VjfHdGpp2fR7975b/8jx8AEVRQRkFDsQrAAAAAElFTkSuQmCC");
        }

        .eduardocollado{
            background-image: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADAAAAAwCAMAAABg3Am1AAAAYFBMVEUAAwAHAQIICwYOEA0aHBknKCU0NjE+QjxGSkROUk1TVkhUWVNdYVtkaWNqcWFvdG5+hXyDhYGRk46OlYycoJqmqqSusqy3urXAw7/LzsvY2tfj5eLs7uvx8/D3+fb9//wadFjiAAAAAWJLR0QAiAUdSAAAAAlwSFlzAAALEwAACxMBAJqcGAAAAAd0SU1FB+EFBQoqBItjkCIAAABBdEVYdENvbW1lbnQAQ1JFQVRPUjogZ2QtanBlZyB2MS4wICh1c2luZyBJSkcgSlBFRyB2NjIpLCBxdWFsaXR5ID0gOTAKsEVYkwAABBVJREFUSMeVlut2tCoMhikKSIEiSDiKc/93uYNjO/awf3yZrjWti8ckbw6U9D0lLSbyhkbI+fVGZmVXCKW0/svI48h5NfQ6SS6MrauFENvjlw0gbIzQCX8oneZpmueJMruFNQKU4w8geUEJJdwapVwI4JyR7H210fsA+fgFdMCACOEhl1L3vR8PzMq9C66s5Nz+JEgvfsbzk8q1DUPk0VMBxdmMAc6m/AAaKDxPmMut4gcBJPacNztPb4TS2X3PnFQ/VKEyDKA9gX7UHL2kKBidRP4BsFN4B6XVp4O946dmZ2cUmUzMfwcivh8jClDqJ3BaiYaNWMlkv8VE5DwqJSDVE/giWgN+AkSUx00pwkbOVMd8AWcSA6jVnOcpC4/jRRC34ENMYXjAQ/vQ9TjQQS366YFDazegYRXoElIZ7y/IoEitJOyKLJ/Akku9ARkjpWp1kGupo9g1ei0WIX369BBqf8VE2siBcy6VtptNxVsl0PiivX3KJPJxz6EtE1uk8SGsBt8rFymVsR6C5+wJLN9lLXyWQhljFTpA6RfBjWZMe68o/5T1DiQsvrbCesH1YvxilHR+ZptdlFKjplSmfgcMpUuxQkhMQbk92GCtkdKGsLBpAKjSvt+S5tPEnUEnZgXtelHZ2wBW6FUYMYBJlwNV+kSImrGDYbNaa6Oh7cbtxXvA5E0aNcWi1n4H3IIT7DZErHEFa+dcAPDO+PqsHA5E30/iZMiOvcFrSjkla3EmsHC5Hz1BrcmNLmAKWr8AtLEECMsQ0YWyo6H6LlMtDmpJAbfJbEM+Z+oLeOycQYBgBZYPvB8RpZRKKTkKMk04vPU78Dgq7pNNC8akXjiHPUf0hESS1KSC6w6BfgMePfhtwzXBuJChYOOmfAKRUR3SObWnvQBwq9XYgXxxHmLELVMQyJYwreMLQDH6CRzFb7hMjXHpjAUSlJGDYM5Be51/LuNhDUNa0c6kvbcedcoZGBxH3/8Cdr+uuH09AAYUC66MjIVxvl874RfQQX9sIYRRPow+pxgDVvtri/wCHlUra9fN+YApp5BGHW2sv8/vF3DEZREas0Y3GFcK24fy+b6nPu0CHt2J93e9RVwDGH5cP951Suc++xvYo5XyY42n/CmBVsIPEDvrh5cB9ORwOle9bihSWMO2Gfw7xxRx8mJr171xAXtyEmeRBxjKWo0bQeE46xwhAx0XR213hghGzwslQlhXI9jMsKUWjTrlLM4BsmU/A3sauYxhD4VtxZaduVhsyr6Ua1VOXOhQW/0OUAUxQcAmXxZtU3TX+y+bTG054Z3ZXo8kYNibUUbjBe2yY+RuFO/ImeGWuD/CUfDWOY+ltqjDX8bs16/ndcZRH2O1mCn5H5tf55//ZeBFSy/+T5vIPxr9Z+A/SGudprzcys0AAAAASUVORK5CYII=");
        }
        .mosqueteroweb{
            background-image: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADAAAAAwCAMAAABg3Am1AAAAYFBMVEUDBQEQEQ4hGRIaGxkqGQkyJRonKCY/Kxc0NjQ/NSxCQ0FfQiJZRzNRU1BgYmCDXTJ9alVucG2NfWeAgn+jhF6PkI2hj3zjjTWfoZ6tn47BrJaxs7DCw8DXwqTR1NH4+velZzBdAAAAAWJLR0QAiAUdSAAAAAlwSFlzAAAOxAAADsQBlSsOGwAAAAd0SU1FB+EFBQopGlpB/oIAAASVSURBVEjHXVXbYusoDBQWBoyBmFBSElP3//9yR9jp2VYPCQaNLiMhyDjnITHX1vZ97/3orabxWVJpreYk587n7J0zihgILIzzOBZA73uLsFAEUHPEGcSnnPDHRGaoi7hYTh97hkVXWo0pDX1mk0qJxvvhwUfvhg3oi4Nek0OITXA5ny48fOHLsyJlUkWcCFq0D0jPUC91B86liiQi4qtw4CJ8DQDy+6cvgNZz2auHSq4wF8WmZxdZAcAGoXqfBDEAR0t7dbGWQY+PEpOXbDw8KDJKKYaMnIWivhco4zSlXLI3PMT4ih2hFW4GQmhKYKmWkuJeQR6+JfILkAqnjD0aTPPFao8OyUakBeKkMohLjplLrxwTiKW2gwfQHgtyKIrycey17YOoUkqtBaV2prbiGJVg2kVaLqMpPHEsI29/VrENQRQF+gyvbgBaQZ2EokxiAswipNhGmwxz3pTmwAvCBEAqI90HSDWVFf6hgm4bCJAGpmJvXnGMOVI92RZJFRAibqIjNElYoACS4FMpFMej+f4BUHFDRHGQKWybjP4IYTHAepZPg9YYyujZ2I+EShKj4VBShVYAU/fQj+1mfEMCeRh0g1UfRGwIaHhkiQb292Dnbatfn5/N3NozGNS1ORhE4ycov76+gmWypHJHVZegH18b1Ruvn5/L/phwEaQYCBkdsAXp1d35akmTgx2rtekT3REima3352SZfc0ICY0U7EliQ+yatPfKWqV8o0X09d6P/U7YMTkzupXsPMsoSO25PBI8WGNnspJPPSrTdAOpQTlWYNQR7sQSonDlwkxbJKXmVcPxatdbbfAwhVt7KMvzPGEGEDpRbbhHUo6ogqfZkl0h1ix2aoVgRrmAPQXnkpFxSlNAIi4+Z63CvNJqrV0nG27LsehXX7aorZk0TQJA6dW6fJOb1q2HyWp42EAesCvdgv14hEd/0TThUxtvCO0w+SPvyry+9qC0tloASGNab7ewlAdu7UaP4iaL4YQL1NrC399HBtm7VTzD78ZAkZ2OD/Xq/bHtdN/3j0kGZwSgzuS/v3tAByMZLbQsok/3r4dCPW3/wCV46pldFgCqp4E4ll6kBiB0XvErVG127q/w7NPHC8sxCwxlhEVaT95ujbUGazxbocOiFyyF8NwfWM88xoeSTpLy06T1kh0iyVHZsTN2bcDou+NCiHW5I6gDv0/ZYSkzRS4RuYjgcIUwkdyYWuNKCcCZNwJDRwppjHgoGSbGrM7yMvCpLyFl99aPY2WyG/dOXW5jkplvlLoAPl4xccznotYxPgdYXif/fwhR8pe+yVeuMvK8GVzgnUoRkkQGhAn/YkrG+Tu0XGSmAqAwvpGBgC4I7gMerAFAZhdAjWkh/jAgBYF48IgAiUnDCH3EhFke3wB2YlMSvxAljhjMmZc/LSuMwbFCoEbmvZwqL4AkBSJ3pcj+bRhPcfTmfIzjmCfDGQA/tRWJPwCFOCWzYe6yJ+7iT3YnJz+Ncx6emu4yekb9y8OvD2Sk/im+//mXhz/60Rv1Z1P99vD7SIaN+3N+tcnbDv9fzGgeZ/5sXn+jZf8D5vFZIZ+pzf0AAAAASUVORK5CYII=");
        }
        .podcastlinux{
            background-image: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADAAAAAwCAMAAABg3Am1AAAAYFBMVEW6Sg27URzJYBnAZjrKaS/LfErLhWPZmV7Vm2/SnHngrH/csY/auKTJy8jZyL3gybfhyL/ez8vf0cXS1NHm2N/b3Nnl29Lc3+Lh4d7s49zl6Ovn6ebt8O3y9PH4+vf9//xpIPITAAAAAWJLR0QAiAUdSAAAAAlwSFlzAAAN1wAADdcBQiibeAAAAAd0SU1FB+EFBQosLgaC/nIAAABBdEVYdENvbW1lbnQAQ1JFQVRPUjogZ2QtanBlZyB2MS4wICh1c2luZyBJSkcgSlBFRyB2NjIpLCBxdWFsaXR5ID0gODIKg7FQJgAAApdJREFUSMe1lguzmjAQhUNRL5BISriQlWTj//+X3c1DENS2M+1BYQbPx9k8SBT3v5T4F0AgISKd/whg76rwGyCg9xs3J4UPANtZiIWKgeEdkO2ZKQTdx9fA1l+CfHz8NuQBBO9IByS1O6yEePIfCR9iRcHvgew/QuH+TGQA3U5rRiFwCwR31NqMRORmiLUgpGE4IiE66ZuLEo+CAp0RDymrOw2HKAHJusugGzQVadwDu30BYgswufetp3uP7oqtEKUidBzuEN41H1NHMZAeBTHLOyC5xS30eUYwRohcEdCgEorRD7DM823Zx2AGUtngeSJnv13akzrrPfIA6IfoSnZLBwGEcFWpuKjYxwT45bbAYgG0YTd/NDQnJXtttIJB3Zw2SrtvNWMCwBhrDMydHoZ5MEabs6SEH+3pVImLEtpVzaVSdWUyoL+aTtLRdI1su6ZppDQJqHV9UlV/qy63mllTgK6TRDRfUn8p8jdSNxFoF3qy6F3Vuouo6lqlRpvOgFQg5dQpo6SWWhfAMtBK0aqqFpcllYSzsdxFjjvDsiZr27M8tefWNvVc06Mv9flGbB44S/1CHTux6GL5OvSmH/RIVxioL/p+WODnkIB7nAxTlucTMTlpmif7zX0dH5oBD8A2uhEzIjHGoHlKeTYOj13K9I4BjAeqy42kgY4puzNDRJmtd0cApMVgGmF8VqmV6l5fUQJcWg2m0Y1viOnxxlEl/gNQENisGhwRX3H3yp8R3C5kPAyeXqURpvGN3PNSCWngIDX5Soqn65oRdosxjx7n+uxcNUYKD8t9qgXd9ZXGcNxQEnE9BEQ/vtqBgivl7wXhzaaIL+1X/2HbdUcEPm/swcOGGeOU/N1fB1rQ0nrpMfynPycf9QuEruKuulaDHwAAAABJRU5ErkJggg==");
        }
        .salmorejogeek{
            background-image: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADAAAAAwCAMAAABg3Am1AAAAYFBMVEUcGxwmJSgiJzQ2NTM3RVQ9VYJuUShYVlNEZlJGY8BdZm5IartvcnFQdv9SfrxTfP9Whv+Hhn6Ck51hmP/gkzZpqv9wtv61tKp5v/1k2YjovEvYxHnDxcK60uTy5b3x69cOzPdIAAAAAWJLR0QAiAUdSAAAAAlwSFlzAAALEwAACxMBAJqcGAAAAAd0SU1FB+EFBQoyB5BxWcEAAAHiSURBVEjHldTrmqMgDAbgcCpbZT12prP24P3f5SRKEAWfsl9/1eZtCNDCuOYrl2/OzxYY/1ME8EF8p6BQRCBPjmIHSsQeFIi0Q9MY0zSnm3WYwUjQFUaDNPkeMWiMqoaXz1Ap02REBIwO1d5ok4oNCPdK4mQiGNRieGUyiOOyPKhVtj4joOuW9ZzUY+R+s1Yg1/UPlGQOvRMIutHY5RMlAECo4/DW/GAhiwVIeq6ED6ituAIfwz0I1BUNtwWE48VVf3z4RJYZ6MCUiLN+K+6E++cTjpA6iGP9kuWaBKAjUFtcqqDX1oEvVRYYhwNcbrfLVl+FPc0BOViqv91C/XYWeeBAUf10gXXg6OzyQAA1mKZJ4dbYvrcZYHaABNZPD9s/3u93Xw0cGzo0/meLQAOd1QXrH1T+nmelrI9igE+U4V1a91OF+rl3T5+wJHziGNT+AOC+ln8AbdfxiaGYC0DLaxLCzkWgvYZLcT8Cy7d1BzrNa+qPoOKv2oHQIgVxIhCmcIWg7STEU5+CkUFL96OgA/7BeNBeqQeUgL9e0Bwfh14Ai7YGuBeB0KMz0t2fT/xBWLemX+LfWLziK4jI1RgN5xEMwrLQ4BafRgawCSKUMc0Xz0D1qdiyU6FDqWBwmONc/AL0UaQcBFX61wAAAABJRU5ErkJggg==");
        }
        .ugeek{
            background-image: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADAAAAAwCAMAAABg3Am1AAAAYFBMVEVVMZZcL5ljMJVdM5VlMphnNJllNpNtNpdxOZt4PJiCPZ2KQZ2RRJyYRJ+gSJ+oTJ6vTKK3UaK/UKXFVKPOVKjMWaPVWajcWKrbXKXkXarqYKjyYKz1Y67/ZK76Zqz+aq9CAXa/AAAAAWJLR0QAiAUdSAAAAAlwSFlzAAALEwAACxMBAJqcGAAAAAd0SU1FB+EFBQorIK57RbIAAAF5SURBVEjH7ZVhc4MgDIYrHEMEI5rikEr8//9ytLVrxR12X3d7T4RwPJhwJJ7YL3X6SwDXRckcgLjEkpZBbABNh7IbAAl4yfMq7fgKVCHqbImQG1Mui3wFptjcBsp7dV9R+xz4yAHVKO2lrGtn2DDIUbcHQKs19HxAp6YOLAbkbwCOC/QAPVgT8Mgl6Zxs3aiNQ+WcQdOLMsCqam337jDox3k+9oWXMy4AYoJRpXC59BXnLD1VGhaBUweTV3im2o96DDZ4S6oAfAbEhuEoPEiGAqxHGcpfYIDQTpq0NZ1xQ4f9pRS0Sa0FVvfAAVjXKug4lICfJSkDCIeydkA80A4Y+q1sZmZAyGOYqBhDStFObNSft7ahmb8CTcryjcd7G7ZlRoflKYrXd7x36xTkheyUcnOVitPVwGi/5xQvlUoXb8nWRnqvtipabpWDX8i8BYw0rLcqknwD8M9lY7zIA2Ca54Xmhy4Uk6FKgJ93CnXZJbHTH/4p/gMFfQHdIENuISGquQAAAABJRU5ErkJggg==");
        }
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
            min-height: 70px;
            background-color: #fff;
            padding: 10px;
            margin: 0 auto;
            margin-bottom: 20px;
        }
        audio {
            width:300px; /* Ancho del reproductor */
            display: block;
            float:left;
        }
        ul {
          list-style-type: none;
        }        
        li {
            list-style-type: none;
            height:70px;
        }
        span[id^="item-"]{
            height:48px;
            line-height: 20px;
            display: block;
            }
        .logo{
            float:left;
            width:48px;
            height:48px;
            margin-right: 5px;
        }
        .title{
            display: block;
            font-size: 18px;
            }
        .mp3, #episode, #podcaster{
            display: block;
            font-size: 14px;
        }
        #player{
            height:80px;
            float:left;
        }
        #playing{
            height:80px;
            float:left;
        }
        .playingnow{
            font-size: 12px;
            color: #9E9E9E;
        }
        @media only screen and (min-width: 700px) {
            .panel{
                width:600px;
            }

        }
    </style>
</head>
<body>
    <div class="panel">
        <div id="player">
            <a href="#" id="left" onclick="return false" title="Anterior"></a>
            <audio id="audio" preload="auto" tabindex="0" controls="">
                <source src="https://ia801502.us.archive.org/5/items/051.AdisBloggerHolaGithub/051.%20Adi%C3%B3s%20Blogger,%20Hola%20Github%20.mp3">
            </audio>
            <a href="#" id="right" onclick="return false" title="Siguiente"></a>
        </div>
        <div id="playing">
            <span class="playingnow">Reproduciendo ahora...</span>
            <span id="podcaster">uGeek</span>
            <span id="episode">Title</span>
        </div>
    </div>
    <div class="panel">
        <ul id="playlist">

'''
HTML_END='''        </ul>
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
        try:
            cursor.execute('''INSERT INTO podcasts(podcast, entry_id, entry_date, entry_title, entry_url)
                              VALUES(?, ?, ?, ?, ?)''',
                           (podcast, entry_id, entry_date, entry_title,
                            entry_url))
        except sqlite3.IntegrityError as e:
            print(e)
            return
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
        fmd.write('# Podcast\n\n')
        fmd.write('## Ultimos podcasts\n')
        for podcast in latest:
            fmd.write('* [{0} - {1}]({2})\n'.format(podcast[0],
                                                    podcast[1],
                                                    podcast[2]))
        for podcast in PODCASTS:
            latest = self.get_latest_podcast(podcast=podcast['name'])
            fmd.write('\n## {0}\n'.format(podcast['name']))
            for podcast in latest:
                fmd.write('* [{0}]({1})\n'.format(podcast[1], podcast[2]))
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
            fhtml.write(HTML_START + '\n')
            for index, row in enumerate(rows):
                fmd.write('{0} - [{1}]({2})\n'.format(row[0], row[1], row[2]))
                fp.write(RECORD_MARKER + ':-1,{0} - {1}\n'.format(row[0],
                                                                  row[1]))
                fp.write('{0}\n'.format(row[2]))
                if index == 0:
                    fhtml.write('<li class="active">\n')
                else:
                    fhtml.write('<li>\n')
                fhtml.write('<span id="item-{0}">\n'.format(index))
                fhtml.write('<span class="logo {0}"></span>\n'.format(
                    row[0].replace(' ', '').lower()))
                fhtml.write('<span class="title">{0}</span>\n'.format(
                    row[0]))
                fhtml.write('<span class="mp3">\n')
                fhtml.write('<a href="{1}">{0}</a>\n'.format(
                    row[1], row[2]))
                fhtml.write('</span>\n')
                fhtml.write('</span>\n')
                fhtml.write('</li>\n')
            fhtml.write(HTML_END + '\n')
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
    db.update_podcasts()
    db.create_m3u()
    print(db.get_latest_podcast())
    print(db.create_md())
    exit(0)
