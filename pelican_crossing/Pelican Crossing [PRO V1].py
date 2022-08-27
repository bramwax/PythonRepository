from tkinter import *

class PelicanCrossing:
    def __init__(self, master):
        ## Set window size, disable ability to resize, and add icon and title
        master.geometry("500x350")
        master.resizable(width=FALSE, height=FALSE)
        master.wm_iconbitmap("images\STA.ico")
        master.title("Pelican Crossing Simulator")

## 1) Create new tkinter window (main parent window) and assign it to the variable root
## 2) Create a new PelicanCrossing object passing it the tkinter window'root' object as a parameter
## 3) Execute the application
## ------------------------------------------------------------------------------------------------
root = Tk()
application = PelicanCrossing(root)
root.mainloop()
