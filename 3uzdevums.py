#nobildēt kadru no webcam 
import cv2
import time
import os
folder = "imagesTaken"
if not os.path.exists(folder):
    os.makedirs(folder)
cap = cv2.VideoCapture(0) #0 nozīmē noklusējuma kameru
while True:
    ret, frame = cap.read()
    cv2.imshow("Main webcam", frame)
    key = cv2.waitKey(1)  
    if key == ord('w'):
        timeTaken = time.time()
        filename = f"{folder}/{timeTaken}.jpg"
        cv2.imwrite(filename, frame)
        print("Image saved!")
    if key == ord('q'): #gaida taustiņa nospiešanu un pārbaude ik pēc 1ms
        break
cap.release()
cv2.destroyAllWindows()