import cv2
import os
import random
import subprocess
import psutil

VIDEO_FOLDER = r"C:\Users\HP\Videos\video"

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

cap = cv2.VideoCapture(0)
video_process = None

def kill_video(proc):
    if proc and proc.poll() is None:
        for p in psutil.Process(proc.pid).children(recursive=True):
            p.terminate()
        proc.terminate()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    eyes_closed = False

    for (x, y, w, h) in faces:
        roi_gray = gray[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        if len(eyes) == 0:
            eyes_closed = True
        break  # Only check first face

    if eyes_closed:
        if video_process is None:
            videos = [os.path.join(VIDEO_FOLDER, v) for v in os.listdir(VIDEO_FOLDER) if v.endswith((".mp4",".avi",".mov"))]
            if videos:
                video_choice = random.choice(videos)
                video_process = subprocess.Popen(['start', '', video_choice], shell=True)
    else:
        kill_video(video_process)
        video_process = None

    cv2.imshow("Eye Tracker", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

kill_video(video_process)
cap.release()
cv2.destroyAllWindows()
