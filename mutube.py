import vlc
import pafy
import time
from moviepy import *
from progress.bar import Bar
import requests
import json
from os import system, name
import random
from youtube_search import YoutubeSearch
import keyboard
import webbrowser

def clear():
  
    # for windows
    if name == 'nt':
        _ = system('cls')
  
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

isskipped = False

def doskip():
    isskipped = True
    time.sleep(1)
    isskipped = False


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
            songtoadd = input("Song name to add to saved list (type exitThis to stop adding): \n")
            try:
                if(songtoadd.lower() == "exitthis"):
                    startfunc.hasexited = True
                else:
                    songfile = open("./Save files/custom.txt", "a+")
                    if(len(songfile.readline()) > 1):
                        print("adding song...")
                        songfile.write("\n")
                        results = YoutubeSearch(songfile, max_results=1).to_dict()
                        for i in results:
                            thevar = "https://www.youtube.com" + i['url_suffix']
                        songfile.write(thevar)
                        print("added song successfully")
                    else:
                        results = YoutubeSearch(songfile, max_results=1).to_dict()
                        for i in results:
                            thevar = "https://www.youtube.com" + i['url_suffix']
                        songfile.write(thevar)
                        print("added song successfully")
                    songfile.close()
            except:
                print("an error has occured. Please report the bug, and do not use this function until fixed.")
                time.sleep(2)
                quit
        startfunc()
    if(Songcount.lower() == "delete"):
        songfile = open("./Save files/custom.txt", "w+")
        songfile.write("https://www.youtube.com/watch?v=7nQ2oiVqKHw")
        print("successfully deleted.")
        startfunc()
    if(Songcount.lower() == "help"):
        print("\n Custom: Load and play all saved songs \n",
            "Save: Add a song (name) to saved songs \n",
            "delete: Remove all songs from saved songs \n",
            "Simply inserting a number here, will state the ammount of songs you wish to play right now. (has to be done) \n",
            "Simply add all the names for the songs you wish to play now. (in order of course) \n")
        startfunc()
        

    else:
        try:
            for l in range(int(Songcount)):
                Songlink = input("Song (enter song name) number " + str(l + 1) + ": \n")
                print("adding song...")
                results = YoutubeSearch(Songlink, max_results=1).to_dict()
                for i in results:
                    thevar = "https://www.youtube.com" + i['url_suffix']
                startfunc.songlist += [thevar]
                print("added song successfully")
        except: 
            if(Songcount == "custom" or Songcount == "save"):
                print("Loading...")
            else:
                print("Error: Invalid number")
                time.sleep(0.5)
                print("exiting...")
                time.sleep(1)

startfunc()

#https://www.youtube.com/watch?v=dQw4w9WgXcQ
def stopwatch(seconds):
    start = time.time()
    time.clock()    
    elapsed = 0
    while elapsed < seconds:
        elapsed = time.time() - start
        stopwatch.converted = str(int((elapsed / playsong.video.length) * 100))
        if(playsong.jsonn["title"] == "Microsoft Windows XP Startup Sound"):
            print("Loading songs...")
        else:
            print("now playing: " + playsong.jsonn["title"] + " \n",
                "seconds: %02d" % (elapsed) + " / " + str(playsong.theothervar),
                " " + stopwatch.converted +"%", "  \n",
                playsong.jsonn["title"], ": \n","▮" * int (stopwatch.converted),
                "▯" * int(100 - float(stopwatch.converted) - 1), "| \n", " (press and hold) S to skip, B to loop, X to open in browser")
        time.sleep(0.2)  
        if keyboard.is_pressed('x'):
            print("opening in brower...")
            webbrowser.open(playsong.thelink)
        elif keyboard.is_pressed('s'):
            print("skipping... (keep holding s if it doesnt skip immediately)")
            return False
            
        clear()

#



def playsong(link):
    r = requests.get("https://noembed.com/embed?url=" + link)
    results = YoutubeSearch(link, max_results=1).to_dict()
                
    try:
        playsong.jsonn =json.loads(r.text)
        for i in results:
            playsong.theothervar = i['duration']
            playsong.thelink = "https://www.youtube.com" + i['url_suffix']

    except:
        playsong.jsonn ="could not load name"
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



