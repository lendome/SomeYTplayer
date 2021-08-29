import vlc
import pafy
import time
from moviepy import *
from progress.bar import Bar
import requests
import json
from os import system, name
import random


#clear is responsible of clearing all messages on screen.
def clear():
  
    # for windows
    if name == 'nt':
        _ = system('cls')
  
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

    




input("press enter to load in")


## --Lines below not in use yet-- ##

#the_program_to_hide = win32gui.GetForegroundWindow()
#win32gui.ShowWindow(the_program_to_hide , win32con.SW_HIDE)

## --Lines above not in use yet-- ##


instance = vlc.Instance()
player = instance.media_player_new()

print("created player")
clear()
# start function: The whole process of setting things up for playback. (still fixing some save issues)
def startfunc():
    startfunc.songlist = []
    startfunc.hasexited = False


    ###
    """

    While it asks about the amount of songs to play,
    
    it accepts other commands like custom,

    save, delete and help, ill find a way to make this useful at some point.
    
    """
    ###


    Songcount = input("How many songs to play? [custom, save, delete, help] \n")

    # when using command "custom" it opens the custom.txt file to check what songs were saved. could be encrypted but low usage is the goal.

    if(Songcount.lower() == "custom"):
        print("adding custom...")
        songfile = open("./Save files/custom.txt", "r")
        for line in songfile.readlines():
            startfunc.songlist += [line]
        print(startfunc.songlist)
        songfile.close()

    # when using command "save" it opens the custom.txt file to add the link you typed in. could be encrypted but low usage is the goal.

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

    # when using command "delete" it opens the custom.txt file to remove all links you added. could be encrypted but low usage is the goal.

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
            # for as many songs you decided to put, it will ask for the link, then add it to the que.
            for l in range(int(Songcount)):
                Songlink = input("Song number " + str(l + 1) + ": \n")
                startfunc.songlist += [Songlink]
        except: 
            # this is if you used one of the commands. 
            if(Songcount == "custom" or Songcount == "save"):
                print("Did not load a number")
            else:
                # this is if the number you entered is not readable

                print("Error: Invalid number")

startfunc()
## -- Lines below is rickroll -- ##
#https://www.youtube.com/watch?v=dQw4w9WgXcQ
# This function (stopwatch) is responsible of letting the song play exactly for its duration, while counting seconds, 
# and calculating the percentage that has passed. This is also used for the progress bar 
# (which i probably solved badly.)
def stopwatch(seconds):
    start = time.time()
    time.clock()    
    elapsed = 0
    while elapsed < seconds:
        elapsed = time.time() - start
        stopwatch.converted = str(int((elapsed / playsong.video.length) * 100))

        ## Now, this long print function may be confusing. What it does, is: ##
        ## -displaying the song name first                                   ##
        ## -showing the time you are into the song and the total duration    ##
        ## -showing the percentage                                           ##
        ## -showing the progress bar                                         ##

        print("now playing: " + playsong.jsonn["title"] + " \n",
            "seconds: %02d" % (elapsed) + " / " + str(playsong.video.length),
            " " + stopwatch.converted +"%", "  \n",
            playsong.jsonn["title"], ": \n","▮" * int (stopwatch.converted),
            "▯" * int(100 - float(stopwatch.converted) - 1), "| \n", "S to skip, B to loop")


        time.sleep(1)  

        
        clear()

#


# This function (playsong) is responsible for actually getting the link and playing it back 
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

    ## -- Lines below not in use -- ##

    #time.sleep(video.length)

    ## -- Lines above not in use -- ##

# This will play every song in the list, unless its invalid. if it is invalid, it will play never gonna give you up, cause you know.
for song in startfunc.songlist:
    try:
        playsong(song)
    except: 
        print("invalid link")
        playsong("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

## -- Lines below not in use -- ##

#while True:
            #self.progressBar.setValue(stopwatch.converted)

## -- Lines above not in use -- ##



