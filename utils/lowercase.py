#!/usr/bin/python
# -*- coding: utf-8 -*-

import glob, re
import commands

dirs = glob.glob('songs/*')
for dirname in dirs:
    # lowercase    
    ret = commands.getoutput('git mv ' + dirname + ' ' + dirname.lower())

reCover = re.compile('(?<=cov=)(.(?<![,\\]\\}]))+')

songs = glob.glob('songs/*/*.sg')
for s in songs:
    with open(s, 'r+') as f:
        data   = f.read()
        match  = reCover.search(data.replace("{",""))
        if match:
            cover = match.group(0)
            data = data.replace(cover, cover.lower())
            f.seek(0)
            f.write(data)
            f.truncate()

            




