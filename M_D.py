import cv2
import numpy as np

def get_frame_gray(cap):
    ret, frame = cap.read()
    frame = frame[:,130:550]
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray,(21,21)0)
    return frame, gray



