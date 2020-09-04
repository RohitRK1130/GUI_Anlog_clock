import tkinter
from PIL import Image,ImageDraw,ImageTk
from datetime import*
import time
from math import*

class clock:
    def __init__(self,root):
        self.root = root
        self.root.title("ANALOG CLOCK")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="#800000")

        title=tkinter.Label(self.root, text="Analog Clock", font=("Times", 50, "bold"), bg="#DC143C", fg="white")
        title.pack()
        self.lbl=tkinter.Label(self.root, bg= "white", bd=20, relief=tkinter.RAISED)
        self.lbl.place(x=470,y=150,height=400,width=400)
        #self.clock_img()
        self.wark()
    def clock_img(self,hr,mi,se):
        clock = Image.new("RGB",(400,400),(255,255,255))
        draw = ImageDraw.Draw(clock)
        bg=Image.open("cl.png")
        bg=bg.resize((300,300),Image.ANTIALIAS)
        clock.paste(bg,(50,50))
        origin = 200,200
        draw.line((origin,200+50*sin(radians(hr)),200-50*cos(radians(hr))), fill="black", width=7)
        draw.line((origin,200+80*sin(radians(mi)),200-80*cos(radians(mi))), fill="blue", width=4)
        draw.line((origin,200+100*sin(radians(se)),200-100*cos(radians(se))), fill="green", width=3)
        draw.ellipse((195,195,210,210),fill="black")
        clock.save("clock_new.png")
    def wark(self):
        h=datetime.now().time().hour
        m=datetime.now().time().minute
        s=datetime.now().time().second
        #print(h,m,s)
        hr=(h/12)*360
        mi=(m/60)*360
        se=(s/60)*360
        #print(hr,mi,se)
        self.clock_img(hr,mi,se)
        self.img = ImageTk.PhotoImage(file="clock_new.png")
        self.lbl.config(image=self.img)
        self.lbl.after(200,self.wark)

root = tkinter.Tk()
obj = clock(root)
root.mainloop()