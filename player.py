import os
import pygame
from pygame import mixer
songs = {}

def hashmapify():
    for file in os.listdir("..\Music"):
        file_path = os.path.join("..\Music", file)
        index = file.find('.')
        id = file[:index]
        songs.update({id:file_path})
    print(songs)

def player_init():
    mixer.init()

def play(trackID:str):
    music_file = str(songs.get(trackID))
    mixer.music.load(music_file)
    mixer.music.play()
    return mixer.music