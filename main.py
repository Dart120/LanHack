from __future__ import print_function, unicode_literals
from PyInquirer import prompt
import pickle
from player import play,player_init,hashmapify
from time import time
import os
import numpy as np
import random
import sys
from people_detect import count_ppl
player_init()
with open('bpm.pkl', 'rb') as f:
    bpm = pickle.load(f)
sim = np.load('similarity_matrix.npy')
hashmap = hashmapify()

questions = [
    {
        'type': 'input',
        'name': 'first_song',
        'message': 'Please give the index of the first song you would like to play?',
    }
]
like_prompt = [
    {
        'type': 'confirm',
        'name': 'liked',
        'message': 'Do you like this song?',
    }
]

answers = prompt(questions)
idx = answers['first_song']
old_vibe = 0
while True:
    path = hashmap[idx]
    player = play(path)
    print("PLAYING - ", os.path.basename(path))
    start = time()
    vibe_checked = False
    like_checked = False
    liked = False
    while player.get_busy():
        if time() - start > 5 and not vibe_checked:
            print("Assessing Vibeee......")
       
            people, distance = count_ppl(20)
            if people:
                dist_per_person = distance/people
            else:
                dist_per_person = 0
            bigger_vibe = dist_per_person > old_vibe
            if bigger_vibe:
                print("It's popping off, will play a faster one")
            else:
                print('Its cooling off, will play a slower one')
            old_vibe = dist_per_person
            vibe_checked = True
        if time() - start > 90 and not like_checked:
            print("Assessing Like......")
            like_answers = prompt(like_prompt)

            liked = like_answers['liked']
            if liked:
                print("Since you liked this song, we'll try and Find you one like it")
            else:
                print("OK OK OK we hear you, we'll play something different")
            like_checked = True
    file_name = os.path.basename(path)
    idx = int(file_name.find('.'))
    if liked:
        ind = np.argpartition(sim[idx], -50)[-50:]
    else:
        ind = np.argpartition(sim[idx], 50)
    bpm_of_songs = list(map(lambda x: (bpm[x],x),ind))
    bpm_of_songs.sort(key=lambda x: x[0])
    
    if bigger_vibe:
        next_idx = random.choice(bpm_of_songs[25:])[1]
    else:
        next_idx = random.choice(bpm_of_songs[:25])[1]
    idx = str(next_idx)



    




# music_process = multiprocessing.Process(target=play, args=(answers['first_song'],))
# music_process.start()
# music_process.join()
# play the song
# analyse mood while
# pick a new song

