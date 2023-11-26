import os
import pygame
from pygame import mixer
def player_init():
    mixer.init()

def play(track:str):
    music_file = ".\Music\\"+track
    mixer.music.load(music_file)
    mixer.music.play()
    while mixer.music.get_busy(): 
        pygame.time.Clock().tick(10)

