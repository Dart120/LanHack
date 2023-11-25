import librosa
def song_to_bpm(path):
    audio_file = librosa.load(path)
    y, sr = audio_file
    tempo = librosa.beat.beat_track(y=y, sr=sr)
    return tempo[0]
if __name__ == "__main__":
    print(song_to_bpm('gigolo.mp3'))