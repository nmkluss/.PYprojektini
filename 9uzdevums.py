import tkinter as tk

class mainWindow:
    def __init__(self):
        self.root = tk.Tk()
        
        self.label = tk.Label(self.root, text="some text", font=('Ariel', 18))
        self.label.pack(padx=10, pady=10)

        self.textbox = tk.Text(self.root, text="more text", height=5, font=('Ariel', 16))
        self.textbox.pack(padx=10, pady=10)

        self.checkState = tk.IntVar() 
        self.check = tk.Checkbutton(self.root, text="check something", font=('Ariel', 16), variable=self.checkState )
        self.check.pack(padx=10, pady=10)
         
        self.button = tk.Button(self.root, text="button text", font=('Ariel', 16), command=self.show_message) 
        self.root. mainloop()

    def show_message(self):
        print("Hello world!")

mainWindow()