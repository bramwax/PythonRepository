from tkinter import *
import winsound, sys
import random

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
    lightsOn = "Green"
    def __init__(self, master):    
        ## Import canvas images
        self.stage = PhotoImage(file="images/stage/stage.png", width=500, height=350)
        self.header = PhotoImage(file="images/stage/header.png", width=500, height=56)
        self.footer = PhotoImage(file="images/stage/footer.png", width=500, height=6)
        self.btnUp = PhotoImage(file="images/crossing/btn_Up.png", width=19, height=19)
        self.btnDwn = PhotoImage(file="images/crossing/btn_Dwn.png", width=19, height=19)
        self.wait = PhotoImage(file="images/crossing/wait.png", width=178, height=100)
        self.red_man = PhotoImage(file="images/crossing/red_man.png", width=178, height=57)
        self.green_man = PhotoImage(file="images/crossing/green_man.png", width=178, height=57)
        self.green_lights = PhotoImage(file="images/crossing/green_lts.png", width=237, height=87)
        self.amber_lights = PhotoImage(file="images/crossing/amber_lts.png", width=237, height=87)
        self.red_lights = PhotoImage(file="images/crossing/red_lts.png", width=237, height=87)
        self.cars_left = [PhotoImage(file="images/cars/red_left.png", width=56, height=99), \
                          PhotoImage(file="images/cars/blue_left.png", width=56, height=99), \
                          PhotoImage(file="images/cars/orange_left.png", width=56, height=99), \
                          PhotoImage(file="images/cars/green_left.png", width=56, height=99)]
        self.cars_right = [PhotoImage(file="images/cars/green_right.png", width=56, height=99), \
                           PhotoImage(file="images/cars/red_right.png", width=56, height=99), \
                           PhotoImage(file="images/cars/blue_right.png", width=56, height=99), \
                           PhotoImage(file="images/cars/orange_right.png", width=56, height=99)]


        ## Create and position canvas
        self.stageCanvas = Canvas(master, width=500, height=350, bd=0, highlightthickness=0)
        self.stageCanvas.place(x=0, y=0)
        ## Add main images to canvas
        self.stageCanvas.create_image(0, 0, image=self.stage, anchor=NW)
        self.stageCanvas.create_image(422, 305, image=self.btnUp, anchor=NW, tag="startBtn")
        self.stageCanvas.create_image(291, 147, image="", anchor=NW, tag="wait")
        self.stageCanvas.create_image(291, 90, image=self.red_man, anchor=NW, tag="man")
        self.stageCanvas.create_image(63, 90, image=self.green_lights, anchor=NW, tag="lights")
        ## Place Cars on canvas and intialise to Red (left) and Green (right)
        self.stageCanvas.create_image(110, 330, image=self.cars_left[random.randint(0,3)], anchor=NW, tags="car_left")
        self.stageCanvas.create_image(246, -50, image=self.cars_right[random.randint(0,3)], anchor=SE, tags="car_right")
        self.moveLeftCars()
        self.moveRightCars()
        ## Place masking images on canvas
        self.stageCanvas.create_image(0, 0, image=self.header, anchor=NW)
        self.stageCanvas.create_image(0, 344, image=self.footer, anchor=NW)

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
        if self.status == "waiting":
            root.config(cursor="arrow")
            self.status = "running"
            self.stopTraffic()

    def changeLights(self, currentLights):
        self.lightsOn = currentLights

    def stopTraffic(self):
        self.stageCanvas.after(10, lambda: self.stageCanvas.itemconfigure("startBtn", image=self.btnUp))
        self.stageCanvas.after(10, lambda: self.stageCanvas.itemconfigure("wait", image=self.wait))
        self.stageCanvas.after(2000, lambda: self.stageCanvas.itemconfigure("lights", image=self.amber_lights))
        self.stageCanvas.after(2000, lambda: self.changeLights("Amber"))
        self.stageCanvas.after(5000, lambda: self.stageCanvas.itemconfigure("lights", image=self.red_lights))
        self.stageCanvas.after(5000, lambda: self.changeLights("Red"))
        self.stageCanvas.after(5500, lambda: self.stageCanvas.itemconfigure("wait", image=""))
        self.stageCanvas.after(5500, lambda: self.pedestrianWalking(29, "off"))
        self.stageCanvas.after(5500, lambda: winsound.PlaySound("sounds/pelican_beep.wav", winsound.SND_ASYNC))

    def pedestrianWalking(self, seconds, image):
        timeRemaining = seconds
        nextImage = image
        if timeRemaining > 0:
            timeRemaining -= 1
            if timeRemaining == 10:
                winsound.PlaySound(None, winsound.SND_PURGE)
                self.restartTraffic(6, "off")
            if image == "off":
                self.stageCanvas.itemconfigure("man", image=self.green_man)
                self.stageCanvas.after(250, lambda: self.pedestrianWalking(timeRemaining, "on"))
            else:
                self.stageCanvas.itemconfigure("man", image="")
                self.stageCanvas.after(250, lambda: self.pedestrianWalking(timeRemaining, "off"))
        else:
            self.stageCanvas.itemconfigure("man", image=self.red_man)

    def restartTraffic(self, seconds, image):
        timeRemaining = seconds
        nextImage = image
        if timeRemaining > 0:
            timeRemaining -= 1
            if image == "off":
                self.stageCanvas.itemconfigure("lights", image=self.amber_lights)
                self.stageCanvas.after(500, lambda: self.restartTraffic(timeRemaining, "on"))
            else:
                self.stageCanvas.itemconfigure("lights", image="")
                self.stageCanvas.after(500, lambda: self.restartTraffic(timeRemaining, "off"))
        else:
            self.stageCanvas.itemconfigure("lights", image=self.green_lights)
            self.changeLights("Green")
            self.moveLeftCars()
            self.moveRightCars()
            self.status = "waiting"

    def moveLeftCars(self):
        self.stageCanvas.move("car_left", 0,-2)
        
        if self.stageCanvas.coords("car_left")[1] < -100:
            self.stageCanvas.itemconfigure("car_left", image=self.cars_left[random.randint(0,3)])
            self.stageCanvas.coords("car_left", 110, 330)
            
        if self.stageCanvas.coords("car_left")[1] > 260 or self.stageCanvas.coords("car_left")[1] < 250 or self.lightsOn == "Green":
            self.stageCanvas.after(20, lambda: self.moveLeftCars())

    def moveRightCars(self):
        self.stageCanvas.move("car_right", 0,2)

        if self.stageCanvas.coords("car_right")[1] > 430:
            self.stageCanvas.itemconfigure("car_right", image=self.cars_right[random.randint(0,3)])
            self.stageCanvas.coords("car_right", 246, -50)
            
        if self.stageCanvas.coords("car_right")[1] > 145 or self.stageCanvas.coords("car_right")[1] < 135 or self.lightsOn == "Green":
            self.stageCanvas.after(20, lambda: self.moveRightCars())

root = Tk()
pelicanSimulator = applicationWindow(root, "Pelican Crossing Simulator")
stageCanvas = stageCanvas(root)
splashCanvas = splashCanvas(root)

root.mainloop()
