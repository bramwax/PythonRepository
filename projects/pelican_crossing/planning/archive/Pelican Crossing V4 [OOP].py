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
        self.splashCanvas.tag_bind("powerBtn", "<Enter>", self.onButtonOver)
        self.splashCanvas.tag_bind("powerBtn", "<Leave>", self.onButtonOut)
        self.splashCanvas.tag_bind("powerBtn", "<ButtonRelease-1>", self.onButtonClick)

    def onButtonOver(self, event):
        if self.status == "waiting":
            root.config(cursor="hand2")
            self.splashCanvas.itemconfigure("powerBtn", image=self.powerBtnDwn)

    def onButtonOut(self, event):
        if self.status == "waiting":
            root.config(cursor="arrow")
            self.splashCanvas.itemconfigure("powerBtn", image=self.powerBtnUp)

    def onButtonClick(self, event):
        root.config(cursor="arrow")
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
        self.btnUp = PhotoImage(file="images/crossing/btn_Up.png", width=19, height=19)
        self.btnDwn = PhotoImage(file="images/crossing/btn_Dwn.png", width=19, height=19)
        self.wait = PhotoImage(file="images/crossing/wait.png", width=178, height=100)
        self.red_man = PhotoImage(file="images/crossing/red_man.png", width=178, height=57)
        self.green_man = PhotoImage(file="images/crossing/green_man.png", width=178, height=57)
        self.green_lights = PhotoImage(file="images/crossing/green_lts.png", width=237, height=87)
        self.amber_lights = PhotoImage(file="images/crossing/amber_lts.png", width=237, height=87)
        self.red_lights = PhotoImage(file="images/crossing/red_lts.png", width=237, height=87)

        ## Create and position canvas
        self.stageCanvas = Canvas(master, width=500, height=350, bd=0, highlightthickness=0)
        self.stageCanvas.place(x=0, y=0)
        ## Add images to canvas
        self.stageCanvas.create_image(0, 0, image=self.stage, anchor=NW)
        self.stageCanvas.create_image(422, 305, image=self.btnUp, anchor=NW, tag="startBtn")
        self.stageCanvas.create_image(291, 147, image=self.wait, anchor=NW, tag="wait")
        self.stageCanvas.create_image(291, 90, image=self.red_man, anchor=NW, tag="man")
        self.stageCanvas.create_image(63, 90, image=self.green_lights, anchor=NW, tag="lights")

        ## Create button events and bind to Power  Button
        self.stageCanvas.tag_bind("startBtn", "<Enter>", self.onButtonOver)
        self.stageCanvas.tag_bind("startBtn", "<Leave>", self.onButtonOut)
        self.stageCanvas.tag_bind("startBtn", "<ButtonRelease-1>", self.onButtonClick)

    def onButtonOver(self, event):
        if self.status == "waiting":
            root.config(cursor="hand2")
            self.stageCanvas.itemconfigure("startBtn", image=self.btnDwn)

    def onButtonOut(self, event):
        if self.status == "waiting":
            root.config(cursor="arrow")
            self.stageCanvas.itemconfigure("startBtn", image=self.btnUp)

    def onButtonClick(self, event):
        root.config(cursor="arrow")
        self.status = "closing"
        self.stageCanvas.itemconfigure("startBtn", image=self.btnUp)


root = Tk()
pelicanSimulator = applicationWindow(root, "Pelican Crossing Simulator")
stageCanvas = stageCanvas(root)
splashCanvas = splashCanvas(root)

root.mainloop()
