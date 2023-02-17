import os
import vlc
from pySmartDL import SmartDL
import threading
import subprocess
import scrapper
from tkinter import *
import json

root = Tk()
root.title("TV-Show Downloader")
root.geometry ("700x400")

name = StringVar()
season = StringVar()
resolution = StringVar()
episode = StringVar()

CONFIG = json.load(open("config.json"))

OBJ = ""
download_name = ""


def start_download (name, season, resolution, episode):
    global OBJ, download_name, CONFIG
    
    if CONFIG["location"] != "":
        if CONFIG["location"][-1] != "/":
            CONFIG["location"] += "/"
    
    page = scrapper.find_page(name)
    if  page != False:
        url, download_name = scrapper.find_link(page, season, resolution, episode)
        
        OBJ = SmartDL(url, CONFIG["location"] + download_name)
        OBJ.start()
        
        

def download ():
    
    semaphore = threading.Semaphore(2)
    threading.Thread(target=start_download, args=(name.get(), season.get(), resolution.get(), episode.get()),).start()

    
    name.set("")
    season.set("")
    resolution.set("")
    episode.set("")
    
    download_button.flash()
    
def pause_download ():
    global is_paused
    
    if is_paused:
        OBJ.resume()
        is_paused = not is_paused
        
    else:
        OBJ.pause()
        is_paused = not is_paused


def terminate_download ():
    global OBJ
    
    OBJ.stop()

def browse_file ():

    default_browser = subprocess.run(["xdg-mime", "query", "default", "inode/directory"],
                                        stdout=subprocess.PIPE).stdout.decode('utf-8').split('.')[-2].lower()

    
    path = CONFIG["location"] + download_name
    threading.Thread(target=os.system, args=(f"{default_browser} {path}",)).start()


def start_browse_file ():
    
    try:
        if OBJ.isFinished():
            browse_file()
            
        else:
            browse_button.flash()
            
    except:
        print ("start download first!")
        
def open_file ():
    path = CONFIG["location"] + download_name
    video_player = subprocess.run(["vlc", path],
                                        stdout=subprocess.PIPE).stdout.decode('utf-8').split('.')[-2].lower()

    
    threading.Thread(target=os.system, args=(f"{video_player} {path}",)).start()
        
def start_open_file ():
    
    try:
        if OBJ.isFinished():
            open_file ()
            
        else:
            open_button.flash()
            
    except:
        print ("start download first!")
    

name_label = Label(root, text= "TV-Show name: ", font=('vazirmatn', 16))
name_label.grid(row = 0,column=0, padx=5, pady=5)

name_entry = Entry(root, textvariable=name, width=52)
name_entry.grid(row=0, column=1, padx=5, pady=5)

season_label = Label(root, text = "TV-Show season: ", font=("vazirmatn", 16))
season_label.grid (row = 1, column=0, padx=5, pady=5)

season_entry = Entry(root, textvariable=season, width=52)
season_entry.grid (row=1, column=1, padx=5, pady=5)

resolution_label = Label(root, text="TV-Show resolution: ", font = ("vazirmatn", 16))
resolution_label.grid (row=2, column=0, padx=5, pady=5)

resolution_entry = Entry(root, textvariable=resolution, width=52)
resolution_entry.grid (row=2, column=1, padx=5, pady=5)

episode_label = Label(root, text="TV-Show episode: ", font = ("vazirmatn", 16))
episode_label.grid (row=3, column=0, padx=5, pady=5)

episode_entry = Entry(root, textvariable=episode, width=52)
episode_entry.grid (row=3, column=1, padx=5, pady=5)

download_button = Button(root, text="Download!", command=download)
download_button.grid(row=4, column=0, padx=1, pady=5)

pause_button = Button(root, text = "Pause / Resume", command=pause_download)
pause_button.grid(row=4, column=1, padx=1, pady=5)

terminate_button = Button(root, text = "Terminate", command= terminate_download)
terminate_button.grid(row = 5, column=0, padx=1, pady=5)

browse_button = Button(root, text="Open in folder", command=start_browse_file)
browse_button.grid(row=5, column=1, padx=1, pady=5)

open_button = Button(root, text= "Open File", command=open_file)
open_button.grid(row = 6, column=0, padx=1, pady=5)


root.mainloop()