import cv2 #for webcams
import datetime #for filedating
import os #for creating image folder 
import numpy as np
import tkinter as tk #for window

folder = "imagesTaken"
if not os.path.exists(folder):
    os.makedirs(folder)

window = tk.Tk()
window.title('3-CamView')
window.geometry("1440x360")

#widgets
cam1_frame = tk.Frame(window, width=480, height=240, background='red')
cam2_frame = tk.Frame(window, width=480, height=240, background='green')
cam3_frame= tk.Frame(window, width=480, height=240, background='blue')
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
cam1_frame.grid(row=0, column=0, sticky='nsew')
cam2_frame.grid(row=0, column=1, sticky='nsew')
cam3_frame.grid(row=0, column=2, sticky='nsew')
button1.grid(row=1, column=0, sticky='nsew')
button2.grid(row=1, column=1, sticky='nsew')
button3.grid(row=1, column=2, sticky='nsew')


#launching the window
window.mainloop()