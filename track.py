#!/usr/bin/env python3
#Python Oldschool Runescape World Tracker
#John Kranz

import urllib.request
import time
import string
import re
import copy

worldDict = {}

popRatio = input("Please enter the population change ratio you wish to track: ")
popRatio = int(popRatio)
timeRatio = input("Please enter the time change ratio you wish to track in seconds: ")

url = urllib.request.urlopen("http://oldschool.runescape.com/slu?order=WmpLA")
data = url.read()
data = data.decode("utf8")
worlds = re.findall("<a[^>]+world=(\d+)'>Old School \d+",data)
population = re.findall("(\d+) players<\/td",data)
worldDict = dict(zip(worlds, population))

#While loop
while True:
    time.sleep(float(timeRatio))
    newurl = urllib.request.urlopen("http://oldschool.runescape.com/slu?order=WmpLA")
    newData = newurl.read()
    newData = newData.decode("utf8")
    newworlds = re.findall("<a[^>]+world=(\d+)'>Old School \d+",newData)
    newpopulation = re.findall("(\d+) players<\/td",newData)
    newworldDict = dict(zip(newworlds, newpopulation))
    for (k, v), (k2,v2) in zip(worldDict.items(), newworldDict.items()):
        change = int(v) - int(v2)
        if(change >= popRatio or change <= -popRatio):
            print(k, change)
    #Clear dictionary and copy new data
    worldDict = {}
    worldDict = dict(zip(newworlds, newpopulation))
    newworldDict = {}
