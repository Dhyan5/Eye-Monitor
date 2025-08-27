# 👁️ Eye State Video Player

A computer vision project that monitors your **eye state** in real-time and automatically plays a random video when you **close your eyes** — like a personal wake-up assistant!

---

## 🧠 Why I Built This

While studying, I often lose focus or start dozing off. I wanted a tool that could **snap me back into focus** the moment I start to drift. So, I built this system:

- It **detects when my eyes close** using computer vision.
- It **instantly plays a random video** (like a meme, motivational clip, or anything loud).
- As soon as I **open my eyes**, the video stops and I’m back on track.

This helps keep me alert and productive while studying!

---

## ✨ Features

✅ Real-time eye detection using **MediaPipe**  
✅ Automatic video playback when **eyes are closed**  
✅ Supports `.mp4`, `.avi`, and `.mov` formats  
✅ Lightweight and runs on **CPU** (no GPU required)  
✅ Quits easily by pressing **`q`**  

---

## 🧰 Prerequisites

Make sure Python is installed. Then install the required packages:

bash
pip install opencv-python
pip install mediapipe
pip install numpy
pip install psutil

---

📁 Setup

Clone this repository or download the script manually.

Create a video folder at the following path and add your videos:

C:\Users\HP\Videos\video


Run the application:

python eye_video_player.py

---

▶️ Usage

When the script runs, your webcam activates.

If you close your eyes, a random video starts playing.

If you open your eyes, the video stops automatically.

Press q anytime to quit the app.

---

📸 How It Works

Uses MediaPipe Face Mesh to detect 468 facial landmarks.

Extracts coordinates for both eyes.

Calculates Eye Aspect Ratio (EAR) to determine whether eyes are closed.

Triggers a random video if EAR drops below a threshold.

---

🔮 Future Ideas

Add sound or text-to-speech alerts

Track how long eyes are closed for drowsiness analytics

Turn it into a productivity timer or Pomodoro tool

Add a GUI for easier interaction
