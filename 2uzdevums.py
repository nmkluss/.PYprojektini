#open the webcam in a seperate window
import cv2
cap = cv2.VideoCapture(0) #0 nozīmē noklusējuma kameru
while True:
    ret, frame = cap.read()
    cv2.imshow("Main webcam", frame)
    if cv2.waitKey(1) == ord('q'): #gaida taustiņa nospiešanu un pārbaude ik pēc 1ms
        break
cap.release()
cv2.destroyAllWindows()
