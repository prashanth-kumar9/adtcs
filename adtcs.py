from tkinter import *
from PIL import ImageTk,Image
import subprocess
import os
from final import count

def enterPath1():
    os.chdir('..\ATCS')
    cmmd1="python main1.py"
    p1=subprocess.Popen(cmmd1, shell=True)
    
    os.chdir('..\ATCS')
    cmmd2="python main2.py"
    p1=subprocess.Popen(cmmd2, shell=True)
    
    os.chdir('..\ATCS')
    cmmd3="python main3.py"
    p1=subprocess.Popen(cmmd3, shell=True)
    
    os.chdir('..\ATCS')
    cmmd4="python main4.py "
    p4=subprocess.Popen(cmmd4, shell=True)
    
    cmmd5="python file1.py"
    subprocess.Popen(cmmd5, shell=True)
    
def signal():
    l=count()
    global my_img, nbutton,  signal1
    os.chdir('..\ATCS')
    cmmd="python final.py"
    p0=subprocess.Popen(cmmd, shell=True)
    signal1=Toplevel()
    my_img=ImageTk.PhotoImage(Image.open("images\signal"+str(l[0])+".jpg"))
    frame1=Label(signal1, image= my_img)
    frame1.grid(column=0, row=0, columnspan=3)
    frame1.pack()
    nbutton=Button(signal1, text="Next Lane", padx=69, pady=10, background='#00ff00',foreground='#ffffff',activebackground='#82f9ff', command=nextlane1)
    nbutton.pack(side= 'right')
    
def nextlane1():
    global my_img, nbutton, signal1
    l=count()
    #frame1.grid_forget()
    signal1=Toplevel()
    my_img=ImageTk.PhotoImage(Image.open("images\signal"  +str(l[1])+ ".jpg"))
    frame1=Label(signal1, image= my_img)
    frame1.grid(column=0, row=0, columnspan=3)
    frame1.pack()
    nbutton=Button(signal1, text="Next Lane", padx=69, pady=10, background='#00ff00',foreground='#ffffff',activebackground='#82f9ff', command=nextlane2)
    
    nbutton.pack(side= 'right')
    
def nextlane2():
    global my_img, nbutton, signal1
    l=count()
    #signal1.destroy
    #frame1.grid_forget()
    signal1=Toplevel()
    my_img=ImageTk.PhotoImage(Image.open("images\signal"  +str(l[2])+ ".jpg"))
    frame1=Label(signal1, image= my_img)
    frame1.grid(column=0, row=0, columnspan=3)
    frame1.pack()
    nbutton=Button(signal1, text="Next Lane", padx=69, pady=10, background='#00ff00',foreground='#ffffff',activebackground='#82f9ff', command=nextlane3)
    
    nbutton.pack(side= 'right')
    
def nextlane3():
    global my_img, nbutton, signal1
    l=count()
    #frame1.grid_forget()
    signal1=Toplevel()
    my_img=ImageTk.PhotoImage(Image.open("images\signal"  +str(l[3])+ ".jpg"))
    frame1=Label(signal1, image= my_img)
    frame1.grid(column=0, row=0, columnspan=3)
    frame1.pack()
    nbutton=Button(signal1, text="Exit", command=signal1.destroy, background='#ff0000', foreground='#ffffff')
    
    nbutton.pack(side= 'right')
    
    
t=Tk()

t.title("SELF ADAPTIVE TRAFFIC SIGNAL CONTROL SYSTEM")
t.geometry('612x349')
myImage= ImageTk.PhotoImage(Image.open("images\dtcs.jpg"))
myLabel1=Label(t, image=myImage)
myLabel1.place(x=0, y=0, relwidth=1, relheight=1)

lane1=ImageTk.PhotoImage(Image.open("images\signal1.jpg"))
lane2=ImageTk.PhotoImage(Image.open("images\signal2.jpg"))
lane3=ImageTk.PhotoImage(Image.open("images\signal3.jpg"))
lane4=ImageTk.PhotoImage(Image.open("images\signal4.jpg"))

my_img=[lane1, lane2, lane3, lane4]



s1=Button(t, text="Start ATCS", padx=69, pady=10, background='#00ff00',foreground='#ffffff',activebackground='#00ff06', command=enterPath1)
s1.pack(side= TOP, padx=60, pady= 60)

s5=Button(t, text="signal", padx=69, pady=10, background='#f8a74b',foreground='#ffffff',activebackground='#82f9ff', command=signal)
s5.pack(side=TOP, padx=50, pady= 20)


buttonQuit=Button(t, text="Exit", command=t.destroy, background='#ff0000', foreground='#ffffff')
buttonQuit.pack(side= BOTTOM)

t.mainloop()