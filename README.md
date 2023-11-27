# SwingSearch: The Automated Swing Dance DJ

## Inspiration

Our love for swing dancing inspired us to develop SwingSearch, a solution aimed at enhancing the swing dance experience. As frequent dancers, we recognized the need for a more dynamic and inclusive DJing approach. Our vision was to create a system that not only selects music automatically but also adapts to the mood of the room, ensuring that no one needs to sit out and miss the fun.

## What It Does

- **Audio Analysis**: Utilizes a cosine similarity matrix to compare songs.
- **BPM Estimation**: Estimates the BPM (Beats Per Minute) of each song using audio analysis.
- **Computer Vision**: Tracks user movement and speed to gauge the room's vibe.
- **Recommender System**: Recommends songs based on their similarity or difference to the current song, tailored to user preferences.

## Usage
```
pip install -r requirements.txt
python3 main.py 2>/dev/null 
```

You may run into trouble with the sort-tracker library with python versions later that 3.6

## How We Built It

- **Technologies Used**: Python, Webflow, Librosa, Figma, and OpenCV.
- **Music Source**: Scraped YouTube for swing songs.
- **Audio Processing**: Used SciPy and Librosa for BPM estimation and frequency domain analysis.
- **Frontend Development**: Designed the interface with Figma and implemented it using Webflow.
- **Cultural Insight**: Gained a deeper understanding of swing culture and skills for the demo through a swing dance lesson.
- **Computer Vision**: Integrated OpenCV with the YOLOv3 model and Simple Online Realtime Tracking (SORT).

## Challenges We Ran Into

- Difficulties with the Spotify API.
- Issues with Webflow integration.
- Computer Vision errors, particularly on MacOS.
- Most team members were first-time hackers.

## Accomplishments That We're Proud Of

- Successfully applied computer vision for the first time.
- Completed demos of both frontend and backend.

## What We Learned

- Gained proficiency in Computer Vision.
- Learned to use Librosa's library for audio analysis.

## What's Next for SwingSearch

- Plans to integrate Spotify and enhance the frontend, which is already quite pretty!



