import cv2 #this is for working with cameras
import datetime #datetime to date the images
import os #for creating/checking image folder
import numpy as np #for manipulating image arrays - combining them
import tkinter as tk #to make the window
from PIL import Image, ImageTk #used to show opencv images in tkinter
import threading #not used here but can be used to run multiple processes at once without freezing the tKinter window
import subprocess #to open the file explorer through window

#check if I have folder for storing screenshots
folder = "imagesTaken"  
if not os.path.exists(folder):
    os.makedirs(folder)

#initialize cameras
cam0 = cv2.VideoCapture(0)
cam1 = cv2.VideoCapture(1)
cam2 = cv2.VideoCapture(3)

#make the tKinter window
window = tk.Tk()
window.title('3-CamView')
window.geometry("1440x400")  # Slightly taller for buttons
window.resizable(False, False) #whether you can resize it (width, height), turned off so layout is as I want it

# Main video display frame
cam_frame = tk.Label(window) #creating a label widget inside window but not used for text
cam_frame.grid(row=0, column=0, columnspan=3, sticky='nsew') #puts this label inside a first row 3collumn layout across the screen

# Placeholder for latest combined image
latest_combined_frame = [None] #this stores the latest combined 3cam view, its a list so it could be changed in a function

# --- Functions ---
def update_video():
    ret0, frame0 = cam0.read() #starts reading frames from all cameras
    ret1, frame1 = cam1.read() #retx is a boolean that is true if a frame is captured
    ret2, frame2 = cam2.read() #framex is the actual frame captured as a numpy array

    if ret0 and ret1 and ret2: #continues only if all 3 cameras are capturing frames 
        # Resize frames to height = 360
        height = 360
        frame0 = cv2.resize(frame0, (int(frame0.shape[1] * height / frame0.shape[0]), height)) #resizes each frame to desired height 
        frame1 = cv2.resize(frame1, (int(frame1.shape[1] * height / frame1.shape[0]), height)) #so the width is proportionally correct
        frame2 = cv2.resize(frame2, (int(frame2.shape[1] * height / frame2.shape[0]), height))

        # Combine frames 
        combined = np.hstack((frame0, frame1, frame2)) #combining all frames in a horizontal frame,np.hstack() stacks arrays horizontally
        latest_combined_frame[0] = combined  # Save latest combined frame for screenshot

        # Convert BGR to RGB for Tkinter
        img_rgb = cv2.cvtColor(combined, cv2.COLOR_BGR2RGB) #converting from BGR to RGB because opencv usees BGR but PIL in tKinter uses RGB
        img_pil = Image.fromarray(img_rgb) #turns the img_rgb which is made from combined from a numpy array into a PIL image
        img_tk = ImageTk.PhotoImage(image=img_pil) #turns the PIL image in a format tKinter understands so we can display openCV images

        # Show image in Tkinter
        cam_frame.imgtk = img_tk #the label we created stores a refference to img_tk tKinter image made by PhotoImage
        cam_frame.configure(image=img_tk) #updates the cam_frame appearance by displaying the webcam img_tk image in the label

    # Repeat after delay
    window.after(15, update_video) #function runs again in 15ms without blocking the window.mainloop()

def take_screenshot():
    if latest_combined_frame[0] is not None: #so if we have a latest frame
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S") #make a timestamp to use as filename 
        filename = f"{folder}/{timestamp}.jpg" #create the file name using a formatted string
        cv2.imwrite(filename, latest_combined_frame[0]) #save the image using imwrite
        print(f"Saved: {filename}")

def open_folder():
    try:
        subprocess.Popen(f'explorer "{os.path.abspath(folder)}"') #opend the imagesTaken in file explored 
    except Exception as e:
        print("Error opening folder:", e)

# --- Buttons ---
button1 = tk.Button(window, text="Something else here", font=('Ariel', 14), bg='gray')
button2 = tk.Button(window, text="Take combined screenshot", font=('Ariel', 14), bg='gray', command=take_screenshot) #calls take_screenshot
button3 = tk.Button(window, text="Open screenshot folder", font=('Ariel', 14), bg='gray', command=open_folder) #calls open_folder

button1.grid(row=1, column=0, sticky='nsew') #positioning the buttons on the second row
button2.grid(row=1, column=1, sticky='nsew')
button3.grid(row=1, column=2, sticky='nsew')

# Grid sizing
window.columnconfigure([0, 1, 2], weight=1) #three columns with equal weight, takes up same space
window.rowconfigure(0, weight=3) #row one takes up the whole lane
window.rowconfigure(1, weight=1) #second row

# Start video update loop
update_video()

# Start GUI
window.mainloop()

# Cleanup on close
cam0.release()
cam1.release()
cam2.release()
cv2.destroyAllWindows()
