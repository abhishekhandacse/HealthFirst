import tkinter as tk
from tkinter import *

def ClearTimer():
    print("Timer Cleared")

def SetTimer():
    print("Timer set")
    print(w.get())


root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

button = tk.Button(frame,
                   text="Set Timer",
                   fg="black",
                   command=SetTimer)
button.pack(side=tk.LEFT)
slogan = tk.Button(frame,
                   text="Clear Timer",
                   command=ClearTimer)
slogan.pack(side=tk.RIGHT)



w = Scale(root, from_=0, to=6, orient=HORIZONTAL)
w.pack()


root.mainloop()