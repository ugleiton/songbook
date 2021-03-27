#!/bin/sh

#send pdf files to patacrep.com
scp volume-1.pdf volume-2.pdf volume-3.pdf volume-4.pdf english.pdf french.pdf naheulbeuk.pdf songbook.pdf lyricbook.pdf ../songbook.tar.gz teamonfi@team-on-fire.com:./www/patacrep/data/documents/ ;

notify-send "Patacrep!" "Uploading files completed" --icon=songbook-client