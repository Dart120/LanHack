import os
import pygame
from pygame import mixer


def hashmapify():
    songs = {}
    for file in os.listdir("Music"):
        file_path = os.path.join("./Music", file)
        index = file.find('.')
        id = file[:index]
        songs.update({id:file_path})
        print(id,file_path)
    return songs

def player_init():
    mixer.init()

def play(path):
  
    mixer.music.load(path)
    mixer.music.play()
    return mixer.music