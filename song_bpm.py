import librosa
import os
import pickle
from tqdm import tqdm
folder_path = 'Music'


def song_to_bpm(path):
    audio_file = librosa.load(path)
    y, sr = audio_file
    tempo = librosa.beat.beat_track(y=y, sr=sr)
    return tempo[0]
if __name__ == "__main__":
    bpm = ['_'] * 500
    for _, entry in tqdm(enumerate(os.listdir(folder_path))):
        full_path = os.path.join(folder_path, entry)
        start = entry.find('.')
        idx = int(entry[:start])
        bpm[idx] = song_to_bpm(full_path)
        print(idx,bpm[idx])
        
    start = bpm.index('_')
    with open('bpm.pkl', 'wb') as fp:
        pickle.dump(bpm, fp)
    bpm = bpm[:start]
    

        
