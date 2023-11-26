import os
import pygame
from pygame import mixer
def player_init():
    mixer.init()

def play(path:str):
    music_file = path
    mixer.music.load(music_file)
    mixer.music.play()
    return mixer.music
    # while mixer.music.get_busy(): 
    #     print('here')
    #     pygame.time.Clock().tick(10)

