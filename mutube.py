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

songlist = []
autosongs = ["https://www.youtube.com/watch?v=dQw4w9WgXcQ",
 "https://www.youtube.com/watch?v=rYLHFMjNZjo",
  "https://www.youtube.com/watch?v=_U0PrwLpb_Q",
   "https://www.youtube.com/watch?v=KB68LQoZHjI",
    "https://www.youtube.com/watch?v=d_HlPboLRL8",
     "https://www.youtube.com/watch?v=PXGycbkbtW0",
      "https://www.youtube.com/watch?v=RkkdYdWMfQ0",
       "https://www.youtube.com/watch?v=hyScwB3ciLM",]

Songcount = input("How many songs to play? (leave blank for one) \n")
if(Songcount == "auto"):
    print("auto adding...")
    for i in range(len(autosongs)):
        songlist += [random.choice(autosongs)]
else:
    try:
        for l in range(int(Songcount)):
            Songlink = input("Song number " + str(l + 1) + ": \n")
            songlist += [Songlink]
    except: 
        print("Error: Invalid number")




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
    
for song in songlist:
    try:
        playsong(song)
    except: 
        print("invalid link")
        playsong("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
#while True:
            #self.progressBar.setValue(stopwatch.converted)



