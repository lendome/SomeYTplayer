import vlc
import pafy
import time
from moviepy import *
from progress.bar import Bar
import requests
import json
from os import system, name
import random

def clear():
  
    # for windows
    if name == 'nt':
        _ = system('cls')
  
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

    




input("press enter to load in")

#the_program_to_hide = win32gui.GetForegroundWindow()
#win32gui.ShowWindow(the_program_to_hide , win32con.SW_HIDE)
instance = vlc.Instance()
player = instance.media_player_new()

print("created player")
clear()

def startfunc():
    startfunc.songlist = []
    startfunc.hasexited = False
    Songcount = input("How many songs to play? [custom, save, delete, help] \n")
    if(Songcount.lower() == "custom"):
        print("adding custom...")
        songfile = open("./Save files/custom.txt", "r")
        for line in songfile.readlines():
            startfunc.songlist += [line]
        print(startfunc.songlist)
        songfile.close()
    if(Songcount.lower() == "save"):
        while startfunc.hasexited == False:
            songtoadd = input("Song link to add to saved list (type exit to stop adding): \n")
            if(songtoadd == "exit"):
                startfunc.hasexited = True
            else:
                songfile = open("./Save files/custom.txt", "a+")
                if(len(songfile.readline()) > 1):
                    songfile.write("\n")
                    songfile.write(songtoadd)
                else:
                    songfile.write(songtoadd)
                songfile.close()
        startfunc()
    if(Songcount.lower() == "delete"):
        songfile = open("./Save files/custom.txt", "w+")
        songfile.write("")
        print("successfully deleted.")
        startfunc()
    if(Songcount.lower() == "help"):
        print("\n Custom: Load and play all saved songs \n",
            "Save: Add a song (link) to saved songs \n",
            "delete: Remove all songs from saved songs \n",
            "Simply inserting a number here, will state the ammount of songs you wish to play right now. \n",
            "Simply add all the links for the songs you wish to play now. \n")
        startfunc()
        

    else:
        try:
            for l in range(int(Songcount)):
                Songlink = input("Song number " + str(l + 1) + ": \n")
                startfunc.songlist += [Songlink]
        except: 
            if(Songcount == "custom" or Songcount == "save"):
                print("Did not load a number")
            else:
                print("Error: Invalid number")

startfunc()

#https://www.youtube.com/watch?v=dQw4w9WgXcQ
def stopwatch(seconds):
    start = time.time()
    time.clock()    
    elapsed = 0
    while elapsed < seconds:
        elapsed = time.time() - start
        stopwatch.converted = str(int((elapsed / playsong.video.length) * 100))
        print("now playing: " + playsong.jsonn["title"] + " \n",
            "seconds: %02d" % (elapsed) + " / " + str(playsong.video.length),
            " " + stopwatch.converted +"%", "  \n",
            playsong.jsonn["title"], ": \n","▮" * int (stopwatch.converted),
            "▯" * int(100 - float(stopwatch.converted) - 1), "| \n", "S to skip, B to loop")
        time.sleep(1)  
        clear()

#



def playsong(link):
    r = requests.get("https://noembed.com/embed?url=" + link)

    playsong.jsonn =json.loads(r.text)
    url = link
    playsong.video = pafy.new(url)
    best = playsong.video.getbestaudio()
    playurl= best.url
    media = instance.media_new(playurl)

    media.get_mrl()
    player.set_media(media)
    player.play()
    stopwatch(playsong.video.length)
    #time.sleep(video.length)

    
for song in startfunc.songlist:
    try:
        playsong(song)
    except: 
        print("invalid link")
        playsong("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
#while True:
            #self.progressBar.setValue(stopwatch.converted)



