from tkinter import *

class mainGUI:
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
        self.splash = PhotoImage(file="images/stage/splash.png", width=500, height=350)

    def createStage(self):
        self.stageCanvas = Canvas(self.master, width=500, height=350, bd=0, highlightthickness=0)
        self.stageCanvas.place(x=0, y=0)
        self.stageCanvas.create_image(0, 0, image=self.stage, anchor=NW)

    def createSplash(self):
        self.splashCanvas = Canvas(self.master, width=500, height=350, bd=0, highlightthickness=0)
        self.splashCanvas.place(x=0, y=0)
        self.splashCanvas.create_image(0, 0, image=self.splash, anchor=NW)

root = Tk()
pelicanApp = mainGUI(root, "Pelican Crossing Simulator")
root.mainloop()
