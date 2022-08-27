from tkinter import *
import winsound

class PelicanCrossing:
    def __init__(self, master):
        ## Create and assign initial values to variables
        self.status = "waiting"

    ## Create main parent window
    ## =====================================================================================================
        ## Set window size, disable ability to resize, and add icon and title
        master.geometry("500x350")
        master.resizable(width=FALSE, height=FALSE)
        master.wm_iconbitmap("images\STA.ico")
        master.title("Pelican Crossing Simulator")

    ## Create splash screen
    ## =====================================================================================================
        ## Import splash screen related images
        self.splash = PhotoImage(file="images/splash/splash.png", width=500, height=350)
        self.splash_fade_3 = PhotoImage(file="images/splash/fade_3.png", width=500, height=350)
        self.splash_fade_2 = PhotoImage(file="images/splash/fade_2.png", width=500, height=350)
        self.splash_fade_1 = PhotoImage(file="images/splash/fade_1.png", width=500, height=350)
        self.powerBtnUp = PhotoImage(file="images/splash/pow_btn_up.png", width=121, height=121)
        self.powerBtnDwn = PhotoImage(file="images/splash/pow_btn_dwn.png", width=121, height=121)
        self.powerBtnClk = PhotoImage(file="images/splash/pow_btn_clk.png", width=121, height=121)

        ## Create and position canvas within mainWindow, then add and position images
        self.splashCanvas = Canvas(master, width=500, height=350, bd=0, highlightthickness=0)
        self.splashCanvas.place(x=0, y=0)
        self.splashCanvas.create_image(0, 0, image=self.splash, anchor=NW, tag="splash")
        self.splashCanvas.create_image(211, 204, image=self.powerBtnUp, anchor=NW, tag="powerBtn")    

        ## Create button events and bind to the Power Button
        self.splashCanvas.tag_bind("powerBtn", "<Enter>", self.onPowerButtonOver)
        self.splashCanvas.tag_bind("powerBtn", "<Leave>", self.onPowerButtonOut)
        self.splashCanvas.tag_bind("powerBtn", "<ButtonRelease-1>", self.onPowerButtonClick)

    def onPowerButtonOver(self, event):
        ## If status is 'waiting' change cursor to hand and swap button images to create hover effect
        if self.status == "waiting":
            root.config(cursor="hand2")
            self.splashCanvas.itemconfigure("powerBtn", image=self.powerBtnDwn)

    def onPowerButtonOut(self, event):
        ## If status is 'waiting' change cursor to 'arrow' and swap button images to create hover effect
        if self.status == "waiting":
            root.config(cursor="arrow")
            self.splashCanvas.itemconfigure("powerBtn", image=self.powerBtnUp)

    def onPowerButtonClick(self, event):
        ## Set cursor to 'arrow' and status to 'closing' (to stop subsequent hover effects when mouseover, etc
        root.config(cursor="arrow")
        self.status = "closing"
        ## Swap button image, play closing sound and progressively display daing canvas background images
        self.splashCanvas.itemconfigure("powerBtn", image=self.powerBtnClk)
        winsound.PlaySound("sounds/start.wav", winsound.SND_ASYNC)
        self.splashCanvas.after(2100, lambda: self.splashCanvas.itemconfigure("powerBtn", image=""))
        self.splashCanvas.after(2350, lambda: self.splashCanvas.itemconfigure("splash", image=self.splash_fade_3))
        self.splashCanvas.after(2400, lambda: self.splashCanvas.itemconfigure("splash", image=self.splash_fade_2))
        self.splashCanvas.after(2450, lambda: self.splashCanvas.itemconfigure("splash", image=self.splash_fade_1))
        # Delete the splash canvas to reveal the stage canvas below
        self.splashCanvas.after(2500, lambda: self.splashCanvas.destroy())

## 1) Create new tkinter window (main parent window) and assign it to the variable root
## 2) Create a new PelicanCrossing object passing it the tkinter window'root' object as a parameter
## 3) Execute the application
## ------------------------------------------------------------------------------------------------
root = Tk()
application = PelicanCrossing(root)
root.mainloop()
