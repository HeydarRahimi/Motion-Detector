import cv2
import numpy as np

def get_frame_gray(cap):
    ret, frame = cap.read()
    frame = frame[:,130:550]
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray,(21,21)0)
    return frame, gray
def bounding_rect(frame,thresh):
    kernel = np.ones((5,5), np.uint8)
    thresh = cv2.dilate(thresh,kernel,iterations=5)
    cnts,_ =cv2.findContours(thresh.copy(),
                             cv2.RETR_EXTERAL,
                             cv2.CHAIN_APPROX_SIMPLE)
    