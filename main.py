from __future__ import print_function, unicode_literals
from PyInquirer import prompt, print_json
from player import play,player_init,hashmapify
from time import time
from people_detect import count_ppl
player_init()
hashmapify()
questions = [
    {
        'type': 'input',
        'name': 'first_song',
        'message': 'Please give the path of the first song you would like to play?',
    }
]

answers = prompt(questions)
print(answers)
player = play(answers['first_song'])
start = time()
vibe_checked = False
while player.get_busy():
    if time() - start > 60 and not vibe_checked:
        print("Assessing Vibeee......")
        print(count_ppl(5))
        vibe_checked = True




# music_process = multiprocessing.Process(target=play, args=(answers['first_song'],))
# music_process.start()
# music_process.join()
# play the song
# analyse mood while
# pick a new song

