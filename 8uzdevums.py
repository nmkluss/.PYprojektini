import tkinter as tk
window = tk.Tk()
window.geometry("1440x480")
window.title("3-CamView") #set the window title

buttonFrame = tk.Frame(window)
buttonFrame.columnconfigure(0, weight=1) #weight 1 is needed to strech the buttons along the x axis
buttonFrame.columnconfigure(1, weight=1)
buttonFrame.columnconfigure(2, weight=1)

button1 = tk.Button(buttonFrame, text="1", font=('Arial', 18))
button1.grid(row=1, column=0, sticky=tk.W+tk.E)
button2 = tk.Button(buttonFrame, text="2", font=('Arial', 18))
button2.grid(row=1, column=1, sticky=tk.W+tk.E)
button3 = tk.Button(buttonFrame, text="3", font=('Arial', 18))
button3.grid(row=1, column=2, sticky=tk.W+tk.E)
buttonFrame.pack(fill='x')
window.mainloop() 

