from tkinter import *
import winsound, sys

class mainGUI:

    status = "idle"
    
    def __init__(self, master, appName):
        self.master = master
        master.geometry("500x350")
        master.resizable(width=FALSE, height=FALSE)
        master.wm_iconbitmap("images\STA.ico")
        master.title(appName)

        self.loadImages()
        self.createStage()
        self.createSplash()

    def loadImages(self):
        ## Load images and assign to variable
        self.stage = PhotoImage(file="images/stage/stage.png", width=500, height=350)
        self.splash = PhotoImage(file="images/splash/splash.png", width=500, height=350)
        self.powerBtnUp = PhotoImage(file="images/splash/pow_btn_up.png", width=121, height=121)
        self.powerBtnDwn = PhotoImage(file="images/splash/pow_btn_dwn.png", width=121, height=121)
        self.powerBtnClk = PhotoImage(file="images/splash/pow_btn_clk.png", width=121, height=121)
        
    def createStage(self):
        self.stageCanvas = Canvas(self.master, width=500, height=350, bd=0, highlightthickness=0)
        self.stageCanvas.place(x=0, y=0)
        self.stageCanvas.create_image(0, 0, image=self.stage, anchor=NW)

    def createSplash(self):
        self.splashCanvas = Canvas(self.master, width=500, height=350, bd=0, highlightthickness=0)
        self.splashCanvas.place(x=0, y=0)
        self.splashCanvas.create_image(0, 0, image=self.splash, anchor=NW)
        self.splashCanvas.create_image(211, 204, image=self.powerBtnUp, anchor=NW, tag="powerBtn")

        ## Create button events and bind to Power  Button
        self.splashCanvas.tag_bind("powerBtn", "<Enter>", lambda event, arg="powerBtn": self.onButtonOver(event, arg))
        self.splashCanvas.tag_bind("powerBtn", "<Leave>", lambda event, arg="powerBtn": self.onButtonOut(event, arg))
        self.splashCanvas.tag_bind("powerBtn", "<ButtonRelease-1>", lambda event, arg="powerBtn": self.onButtonClick(event, arg))

    def onButtonOver(self, event, arg):
        if arg == "powerBtn" and self.status == "idle":
            self.splashCanvas.itemconfigure("powerBtn", image=self.powerBtnDwn)

    def onButtonOut(self, event, arg):
        if arg == "powerBtn" and self.status == "idle":
            self.splashCanvas.itemconfigure("powerBtn", image=self.powerBtnUp)

    def onButtonClick(self, event, arg):
        if arg == "powerBtn":
            self.status = "running"
            winsound.Beep(1000, 50)
            self.splashCanvas.itemconfigure("powerBtn", image=self.powerBtnClk)

            ##winsound.PlaySound("sounds/pelican_beep.wav", winsound.SND_ASYNC)
            self.splashCanvas.after(500, lambda: self.splashCanvas.destroy())


root = Tk()
pelicanApp = mainGUI(root, "Pelican Crossing Simulator")
root.mainloop()
