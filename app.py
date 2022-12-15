import scrapper
from tkinter import *
import requests
import wget
import json
import os

root = Tk()
root.title("TV-Show Downloader")
root.geometry ("700x400")

name = StringVar()
season = StringVar()
resolution = StringVar()
episode = StringVar()

def download ():
    scrapper.start_download(name.get(), season.get(), resolution.get(), episode.get())
    name.set("")
    season.set("")
    resolution.set("")
    episode.set("")
    

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
download_button.grid(row=4, column=1, padx=0, pady=5)



root.mainloop()