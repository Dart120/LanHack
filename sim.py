import os
import librosa
import numpy as np
from scipy.spatial import distance
from tqdm import tqdm
import pickle

# Function to extract audio features (you may want to refine this based on your needs)
def extract_features(file_path):
    y, sr = librosa.load(file_path)
    mfcc = librosa.feature.mfcc(y=y, sr=sr)
    return np.mean(mfcc, axis=1)

# Function to calculate similarity between two songs using cosine distance
def similarity(song1_features, song2_features):
    return 1 - distance.cosine(song1_features, song2_features)

# Directory containing the songs
folder_path = ".\Music"

# List to hold song features and file names
song_features = []
file_names = []
counter = 0

# Extract features for each song in the folder
for idx,file in tqdm(enumerate(os.listdir(folder_path))):
    if file.endswith(".mp3"):  # Adjust file extension as needed
        file_path = os.path.join(folder_path, file)
        features = extract_features(file_path)
        song_features.append(features)
        file_names.append(file)
        index = file.find('.')
        dst = file[index:]
        dst = str(idx)+dst
        os.rename(folder_path + "\\" + file, folder_path + "\\" +dst)
        counter += 1

similarity_array = np.zeros((counter,counter),float)
# Calculate similarity between songs
num_songs = len(song_features)
for i in tqdm(range(num_songs)):
    for j in range(i + 1, num_songs):
        similarity_score = similarity(song_features[i], song_features[j])
        similarity_array[i][j] = similarity_score

np.save("similarity_matrix", similarity_array)

