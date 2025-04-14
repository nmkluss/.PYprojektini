import cv2 
import datetime
import os
import numpy as np

folder = "imagesTaken"
if not os.path.exists(folder):
    os.makedirs(folder)


cam0 = cv2.VideoCapture(0) 
cam1 = cv2.VideoCapture(1)  
cam2 = cv2.VideoCapture(3) 
captureFrames = True
while captureFrames:
    ret0, frame0 = cam0.read()
    ret1, frame1 = cam1.read()
    ret2, frame2 = cam2.read()

    if not (ret0 and ret1 and ret2):
        print("One of the cameras failed to read. Skipping this frame...")
        continue

    height = 360
    frame0 = cv2.resize(frame0, (int(frame0.shape[1] * height / frame0.shape[0]), height))
    frame1 = cv2.resize(frame1, (int(frame1.shape[1] * height / frame1.shape[0]), height))
    frame2 = cv2.resize(frame2, (int(frame2.shape[1] * height / frame2.shape[0]), height))

    combined = np.hstack((frame0, frame1, frame2))
    cv2.imshow("3-Cam View", combined)

    key = cv2.waitKey(1)
    if key == ord('w'):
        timeTaken = datetime.datetime.now()
        timestamp = timeTaken.strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"{folder}/{timestamp}.jpg"
        cv2.imwrite(filename, combined)
        print(f"Image saved as {timestamp}.jpg in {folder}!")
        continue
    elif key == ord('q'):
        break


cam0.release()
cam1.release()
cam2.release()
cv2.destroyAllWindows()