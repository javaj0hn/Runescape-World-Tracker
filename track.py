#!/usr/bin/env python3
#Python Oldschool Runescape World Tracker
#John Kranz

import urllib.request
import time
import string
import re

worldDict = {}

url = urllib.request.urlopen("http://oldschool.runescape.com/slu?order=WmpLA")
data = url.read()
data = data.decode("utf8")
worlds = re.findall("<a[^>]+world=(\d+)'>Old School \d+",data)
population = re.findall("(\d+) players<\/td",data)
worldDict = dict(zip(worlds, population))
