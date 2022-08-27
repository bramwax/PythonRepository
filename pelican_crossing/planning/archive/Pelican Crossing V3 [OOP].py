from tkinter import *
import winsound, sys

class applicationWindow:
    def __init__(self, master, appName):
        self.master = master
        master.geometry("500x350")
        master.resizable(width=FALSE, height=FALSE)
        master.wm_iconbitmap("images\STA.ico")
        master.title(appName)

class splashCanvas:
    status = "waiting"
    def __init__(self, master):    
        ## Import canvas images
        self.splash = PhotoImage(file="images/splash/splash.png", width=500, height=350)
        self.splash_fade_3 = PhotoImage(file="images/splash/fade_3.png", width=500, height=350)
        self.splash_fade_2 = PhotoImage(file="images/splash/fade_2.png", width=500, height=350)
        self.splash_fade_1 = PhotoImage(file="images/splash/fade_1.png", width=500, height=350)
        self.powerBtnUp = PhotoImage(file="images/splash/pow_btn_up.png", width=121, height=121)
        self.powerBtnDwn = PhotoImage(file="images/splash/pow_btn_dwn.png", width=121, height=121)
        self.powerBtnClk = PhotoImage(file="images/splash/pow_btn_clk.png", width=121, height=121)

        ## Create and position canvas, the add background and button images
        self.splashCanvas = Canvas(master, width=500, height=350, bd=0, highlightthickness=0)
        self.splashCanvas.place(x=0, y=0)
        self.splashCanvas.create_image(0, 0, image=self.splash, anchor=NW, tag="splash")
        self.splashCanvas.create_image(211, 204, image=self.powerBtnUp, anchor=NW, tag="powerBtn")    

        ## Create button events and bind to Power  Button
        self.splashCanvas.tag_bind("powerBtn", "<Enter>", lambda event, arg="powerBtn": self.onButtonOver(event, arg))
        self.splashCanvas.tag_bind("powerBtn", "<Leave>", lambda event, arg="powerBtn": self.onButtonOut(event, arg))
        self.splashCanvas.tag_bind("powerBtn", "<ButtonRelease-1>", lambda event, arg="powerBtn": self.onButtonClick(event, arg))

    def onButtonOver(self, event, arg):
        if self.status == "waiting":
            self.splashCanvas.itemconfigure("powerBtn", image=self.powerBtnDwn)

    def onButtonOut(self, event, arg):
        if self.status == "waiting":
            self.splashCanvas.itemconfigure("powerBtn", image=self.powerBtnUp)

    def onButtonClick(self, event, arg):
        self.status = "closing"
        self.splashCanvas.itemconfigure("powerBtn", image=self.powerBtnClk)
        winsound.PlaySound("sounds/start.wav", winsound.SND_ASYNC)
        self.splashCanvas.after(2100, lambda: self.splashCanvas.itemconfigure("powerBtn", image=""))
        self.splashCanvas.after(2350, lambda: self.splashCanvas.itemconfigure("splash", image=self.splash_fade_3))
        self.splashCanvas.after(2400, lambda: self.splashCanvas.itemconfigure("splash", image=self.splash_fade_2))
        self.splashCanvas.after(2450, lambda: self.splashCanvas.itemconfigure("splash", image=self.splash_fade_1))
        self.splashCanvas.after(2500, lambda: self.splashCanvas.destroy())

class stageCanvas:
    status = "waiting"
    def __init__(self, master):    
        ## Import canvas images
        self.stage = PhotoImage(file="images/stage/stage.png", width=500, height=350)

        ## Create and position canvas, the add background and button images
        self.stageCanvas = Canvas(master, width=500, height=350, bd=0, highlightthickness=0)
        self.stageCanvas.place(x=0, y=0)
        self.stageCanvas.create_image(0, 0, image=self.stage, anchor=NW)

root = Tk()
pelicanSimulator = applicationWindow(root, "Pelican Crossing Simulator")
stageCanvas = stageCanvas(root)
splashCanvas = splashCanvas(root)

root.mainloop()
