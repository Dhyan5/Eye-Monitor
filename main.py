import cv2
import mediapipe as mp
import numpy as np
import subprocess
import os
import random
import psutil

video_folder=r"C:\Users\HP\Videos\video"

mediapipe_face_mesh=mp.solutions.face_mesh
face_mesh=mediapipe_face_mesh.FaceMesh(static_image_mode=False,max_num_faces=1)

mediapipe_drawing=mp.solutions.drawing_utils

camera=cv2.VideoCapture(0)
video_process=None

def eye_aspect_ratio(landmarks,indices):
    points=np.array([landmarks[i] for i in indices])
    vertical_1=np.linalg.norm(points[1]-points[5])
    vertical_2=np.linalg.norm(points[2]-points[4])
    horizontal=np.linalg.norm(points[0]-points[3])
    ratio=(vertical_1+vertical_2)/(2.0*horizontal)
    return ratio

def stop_video(process):
    if process and process.poll() is None:
        for child in psutil.Process(process.pid).children(recursive=True):
            child.terminate()
        process.terminate()
        
left_eye_indices=[33,160,158,133,153,144]
right_eye_indices=[362,385,387,263,373,380]

ear_threshold=0.2

while True:
    success,frame=camera.read()
    if not success:
        break

    frame_rgb=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    result=face_mesh.process(frame_rgb)

    eyes_are_closed=False

    if result.multi_face_landmarks:
        for face_landmarks in result.multi_face_landmarks:
            frame_height,frame_width,_=frame.shape
            landmarks=[(int(point.x*frame_width),int(point.y*frame_height)) for point in face_landmarks.landmark]

            left_ear=eye_aspect_ratio(landmarks,left_eye_indices)
            right_ear=eye_aspect_ratio(landmarks,right_eye_indices)
            average_ear=(left_ear+right_ear)/2.0

            if average_ear<ear_threshold:
                eyes_are_closed=True

            mediapipe_drawing.draw_landmarks(
                frame,
                face_landmarks,
                mediapipe_face_mesh.FACEMESH_TESSELATION,
                landmark_drawing_spec=None,
                connection_drawing_spec=mediapipe_drawing.DrawingSpec(color=(0,255,0),thickness=1)
            )
            break

    if eyes_are_closed:
        if video_process is None:
            available_videos=[os.path.join(video_folder,file) for file in os.listdir(video_folder) if file.endswith((".mp4",".avi",".mov"))]
            if available_videos:
                selected_video=random.choice(available_videos)
                video_process=subprocess.Popen(['start','',selected_video],shell=True)
    else:
        stop_video(video_process)
        video_process=None

    cv2.imshow("Eye State Monitor",frame)

    if cv2.waitKey(1)&0xFF==ord('q'):
        break

stop_video(video_process)
camera.release()
cv2.destroyAllWindows()
