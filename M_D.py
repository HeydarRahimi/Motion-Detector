import cv2
import numpy as np

cap= cv2.VideoCapture(0)
def get_frame_gray(cap):
    ret, frame = cap.read()
    frame = frame[:,130:550]
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray,(21,21),0)
    return frame, gray
def bounding_rect(frame,thresh):
    kernel = np.ones((5,5), np.uint8)
    thresh = cv2.dilate(thresh,kernel,iterations=5)
    cnts,_ =cv2.findContours(thresh.copy(),
                             cv2.RETR_EXTERAL,
                             cv2.CHAIN_APPROX_SIMPLE)
     for c in cnts:
        if cv2.contourArea(c) < 100:
            continue
        (x,y,w,h) = cv2.boundingRect(c)
        cv2.rectangle(frame, (x, y), (x+w, y + h), (0, 255, 0), 2)
        _, old_gray = get_frame_gray(cap)
while True:
    frame, gray = get_frame_gray(cap)
    frameDelta = cv2.absdiff (old_gray, gray)
    ret, thresh = cv2.threshold (frameDelta, 10, 255, cv2.THRESH_BINARY)
    bounding_rect(frame, thresh)
    cv2.imshow('detector', frame)
    old_gray = gray
    if cv2.waitKey(1) == 13: 
        break
cap.release()
cv2.destroyAllwindows()
