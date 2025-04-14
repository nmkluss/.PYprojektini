import cv2 #for webcams
import datetime #for filedating
import os #for creating image folder 
import numpy as np
import tkinter as tk #for window

#1)Pārbaudu/izveidoju screenshot folder
folder = "imagesTaken"
if not os.path.exists(folder):
    os.makedirs(folder)

#2)Kameru funkcionalitāte
cam0 = cv2.VideoCapture(0) 
cam1 = cv2.VideoCapture(1)  
cam2 = cv2.VideoCapture(3) 
captureState = True
while captureState:
    ret0, frame0 = cam0.read()
    ret1, frame1 = cam1.read()
    ret2, frame2 = cam2.read()

    if not (ret0 and ret1 and ret2):
        print("One of the cameras failed to read. Skipping this frame...")
        continue

    height = 240
    frame0 = cv2.resize(frame0, (int(frame0.shape[1] * height / frame0.shape[0]), height))
    frame1 = cv2.resize(frame1, (int(frame1.shape[1] * height / frame1.shape[0]), height))
    frame2 = cv2.resize(frame2, (int(frame2.shape[1] * height / frame2.shape[0]), height))

    combined = np.hstack((frame0, frame1, frame2))
#3)Galvenais logs 
window = tk.Tk()
window.title('3-CamView')
window.geometry("1440x360")

#widgets
cam_frame = tk.Frame(window, width=1440, height=240, background='red')
button1 = tk.Button(text="something else here", font=('Ariel', 16), background='gray')
button2 = tk.Button(text="Take combined screenshot", font=('Ariel', 16), background='gray')
button3 = tk.Button(text="Open screenshot folder", font=('Ariel', 16), background='gray')
#making the grid
window.columnconfigure(0, weight = 1) #(index, weight) index meaning basically which collumn and weight decides how wide it will be
window.columnconfigure(1, weight = 1) #three collumns that take up 1/3 of the width of the screen
window.columnconfigure(2, weight = 1) 
window.rowconfigure(0, weight = 1)
window.rowconfigure(1, weight = 1)

#placing a widget
cam_frame.grid(row=0, column=0, sticky='nsew')
button1.grid(row=1, column=0, sticky='nsew')
button2.grid(row=1, column=1, sticky='nsew')
button3.grid(row=1, column=2, sticky='nsew')


#launching the window
window.mainloop()