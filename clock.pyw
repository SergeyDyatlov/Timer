from Tkinter import *
import time
import datetime
from PIL import Image, ImageTk

class App():
    def __init__(self):
        self.root = Tk()
        self.root.title('Dyatlov Timer')
        self.root.wm_iconbitmap('image\\time.ico')
        self.root.geometry('200x70')
        self.root.resizable(0, 0)
        
        #self.root.overrideredirect(True)
        self.frame = Frame(self.root, width=1000, height=100)
        self.frame.pack(side=BOTTOM)

        self.label = Label(text="")
        self.label.pack()
        self.labelTimer = Label(text="")
        self.labelTimer.pack()
        
        copyImage = self.loadImage("image\\copy.gif")
        startImage = self.loadImage("image\\start.gif")
        stopImage = self.loadImage("image\\stop.gif")
        restartImage = self.loadImage("image\\restart.gif")
        
        self.button = Button(self.frame, text="copy", image=copyImage, command=self.copyTimer, fg="BLUE")
        self.button.pack(side=LEFT)
        self.buttonStartTimer = Button(self.frame, text="start", image=startImage, command=self.startTimer, fg="GREEN")
        self.buttonStartTimer.pack(side=LEFT)
        self.buttonStopTimer = Button(self.frame, text="stop", image=stopImage, command=self.stopTimer, fg="RED")
        self.buttonStopTimer.pack(side=LEFT)
        self.buttonRestartTimer = Button(self.frame, text="restart", image=restartImage, command=self.restartTimer, fg="BLACK")
        self.buttonRestartTimer.pack(side=LEFT)

        self.topmost = IntVar()
        self.CheckButton = Checkbutton(
            self.frame, text="Top", bg="#FFFDD0",fg="black", 
            variable=self.topmost,
            command=self.setTopmost)
        self.CheckButton.pack(side=RIGHT)
        
        self.startTime = datetime.datetime.now()
        self.runTimer = 1
        self.tick = 0
        self.update_clock()
        self.updateTimer()
        self.root.mainloop()

    def setTopmost(self):
        print self.topmost.get()
        check = self.topmost.get()
        if check != 0:
            self.root.wm_attributes("-topmost", 1)
        else:
            self.root.wm_attributes("-topmost", 0)

    def loadImage(self, name):
        image = Image.open(name)
        return ImageTk.PhotoImage(image)

    def startTimer(self):
        if self.runTimer != 1:
            self.runTimer = 1
            self.updateTimer()
        
    def stopTimer(self):
        self.runTimer = 0

    def restartTimer(self):
        self.tick = 0
        self.Timer = '%02d:%02d:%02d' % (0, 0, 0)
        self.labelTimer.configure(text=self.Timer)

    def copyTimer(self):
        self.root.clipboard_clear()
        self.root.clipboard_append(self.Timer[0:5])
        
    def update_clock(self):
        now = time.time()
        now = (datetime.datetime.fromtimestamp(int(now)).strftime('%Y-%m-%d %H:%M:%S'))
        self.label.configure(text=now)
        self.root.after(1000, self.update_clock)

    def updateTimer(self):
        if self.runTimer != 0:
            self.tick += 1
            self.Timer = '%02d:%02d:%02d' % (self.tick//3600,(self.tick//60)%60,self.tick%60)
            self.labelTimer.configure(text=self.Timer)
            self.root.after(1000, self.updateTimer)

app=App()
