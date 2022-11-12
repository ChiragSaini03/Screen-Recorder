import pyautogui
from tkinter import *
from sys import exit
from tkinter import filedialog
from tkinter import messagebox
from datetime import datetime
...
win=Tk()
# win.wm_state('iconic')
win.title('Screenshooter')
win.overrideredirect(1)         # win.attributes('-toolwindow', False)  # will remove the top badge of window
win.geometry('950x600')
pyautogui.FAILSAFE = False
win.attributes('-alpha',0.9)
win.wm_attributes('-transparentcolor','light blue')
win.attributes('-topmost',True)
...
colour='yellow'
i=1 
j=1
lastClickX = 0
lastClickY = 0
folder_selected='D:\CHIRAG PERSONAL\Screenshot Saver\Scr_ver'
...

def minwin():
    win.overrideredirect(0)
    win.wm_state('iconic')
    win.overrideredirect(1)

def take_scr():
    global folder_selected
    global var
    global i
    win.attributes('-alpha',0)
    screenposx = win.winfo_x()
    screenposy = win.winfo_y()
    height= win.winfo_height()
    width= win.winfo_width()
    ...
    cc=datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    cc=cc.replace('/','_')
    cc=cc.replace(':','-')
    ...
    x1,y1,x2,y2 = screenposx,screenposy+40,width,height
    pyautogui.screenshot(f'{folder_selected}\{cc}_scr.png',region=(x1,y1,x2,y2))
    win.attributes('-alpha',0.9)
    i+=1
def open_fol():
    global folder_selected
    folder_selected = filedialog.askdirectory()
def close():
    win.destroy()
    exit()
def change():
    global var
    win.attributes('-alpha',var.get())

def h_inc(event=None):
    global can
    height= win.winfo_height()
    width= win.winfo_width()
    can.destroy()
    can=Canvas(win,bg='pink',height=(height+10),width=width,cursor="plus red")
    can.create_rectangle(0,0,width,height+10,fill='light blue',outline=colour,width=40)
    can.grid(row=1,column=1,sticky = N + E + S + W)
    win.geometry(f'{width}x{height+10}')

def h_dec(event=None):
    global can
    height= win.winfo_height()
    width= win.winfo_width()
    if (height-20) > 0 :
        can.destroy()
        can=Canvas(win,bg='pink',height=(height-10),width=width,cursor="plus red")
        can.create_rectangle(0,0,width,height-10,fill='light blue',outline=colour,width=40)
        can.grid(row=1,column=1,sticky = N + E + S + W)
        win.geometry(f'{width}x{height-10}')
def w_inc(event=None):
    global can
    height= win.winfo_height()
    width= win.winfo_width()
    can.destroy()
    can=Canvas(win,bg='pink',height=(height),width=width+10,cursor="plus red")
    can.create_rectangle(0,0,width+10,height,fill='light blue',outline=colour,width=40)
    can.grid(row=1,column=1,sticky = N + E + S + W)
    win.geometry(f'{width+10}x{height}')

def w_dec(event=None):
    global can
    height= win.winfo_height()
    width= win.winfo_width()
    if (width-20) > 0:
        can.destroy()
        can=Canvas(win,bg='pink',height=(height),width=width-10,cursor="plus red")
        can.create_rectangle(0,0,width-10,height,fill='light blue',outline=colour,width=40)
        can.grid(row=1,column=1,sticky = N + E + S + W)
        win.geometry(f'{width-10}x{height}')
def zoomer(event=None):
    global can
    height= win.winfo_height()
    width= win.winfo_width()
    if event.delta>0:
        can.destroy()
        can=Canvas(win,bg='pink',height=(height+20),width=width,cursor="plus red")
        can.create_rectangle(0,0,width,height+20,fill='light blue',outline=colour,width=40)
        can.grid(row=1,column=1,sticky = N + E + S + W)
        win.geometry(f'{width}x{height+20}')
    else:
        if  (height-20) > 0:
            can.destroy()
            can=Canvas(win,bg='pink',height=(height-20),width=width,cursor="plus red")
            can.create_rectangle(0,0,width,height-20,fill='light blue',outline=colour,width=40)
            can.grid(row=1,column=1,sticky = N + E + S + W)
            win.geometry(f'{width}x{height-20}')

def zoomer_ctrl(event=None):
    global can
    height= win.winfo_height()
    width= win.winfo_width()
    if event.delta>0:
        can.destroy()
        can=Canvas(win,bg='pink',height=(height),width=(width+20),cursor="plus red")
        can.create_rectangle(0,0,(width+20),height,fill='light blue',outline=colour,width=40)
        can.grid(row=1,column=1,sticky = N + E + S + W)
        win.geometry(f'{width+20}x{height}')
    else:
        if (width-20) > 0 :
            can.destroy()
            can=Canvas(win,bg='pink',height=(height),width=width-20,cursor="plus red")
            can.create_rectangle(0,0,width-20,height,fill='light blue',outline=colour,width=40)
            can.grid(row=1,column=1,sticky = N + E + S + W)
            win.geometry(f'{width-20}x{height}')

def up(event=None):
    screenposx = win.winfo_x()
    screenposy = win.winfo_y()
    win.geometry(f'+{screenposx}+{screenposy-20}')
def down(event=None):
    screenposx = win.winfo_x()
    screenposy = win.winfo_y()
    win.geometry(f'+{screenposx}+{screenposy+20}')
def left(event=None):
    screenposx = win.winfo_x()
    screenposy = win.winfo_y()
    win.geometry(f'+{screenposx-20}+{screenposy}')
def right(event=None):
    screenposx = win.winfo_x()
    screenposy = win.winfo_y()
    win.geometry(f'+{screenposx+20}+{screenposy}')
def col():
    global colour
    global var1
    global can
    lis_col=['light pink','white','light green']
    colour=(lis_col[var1.get()])
    height= win.winfo_height()
    width= win.winfo_width()
    can.destroy()
    can=Canvas(win,bg='pink',height=height,width=width,cursor="plus red")
    can.create_rectangle(0,0,width,height,fill='light blue',outline=(lis_col[var1.get()]),width=40)
    can.grid(row=1,column=1,sticky = N + E + S + W)
    # can.configure(bg=lis_col[var1.get()])

def start_rec():
    messagebox.showinfo(title='Recording',message="Press 'q' to quit/exit Screen Recording.")

def stop_rec(event=None):
    ...
def hide():
    global j
    j+=1
    if j%2==0:
        win.overrideredirect(1)
    else:
        win.overrideredirect(0)

def SaveLastClickPos(event):
    global lastClickX, lastClickY
    lastClickX = event.x
    lastClickY = event.y


def Dragging(event):
    x, y = event.x - lastClickX + win.winfo_x(), event.y - lastClickY + win.winfo_y()
    win.geometry("+%s+%s" % (x , y))

...
m1=Menu(win)
...
var=DoubleVar()
var.set(0.5)
var1=IntVar()
var1.set(1)
m1.add_command(label='  Scr     ',command=take_scr)
p2=Menu(m1, tearoff=0)
p3=Menu(m1, tearoff=0)
p4=Menu(m1)
#m1.add_cascade(label='  Intensity  ',menu=p2)
m1.add_cascade(label='  Colour  ',menu=p3)
m1.add_cascade(label='  Record  ',menu=p4)
m1.add_command(label='  Folder  ',command=open_fol)
m1.add_command(label='  -  ',command=minwin)
m1.add_command(label='  X  ',command=close)
# m1.add_command(label='  ↑↑↑   ',command=hide)
# p2.add_radiobutton(label='20',variable=var,value=0.2,command=change)
# p2.add_radiobutton(label='40',variable=var,value=0.4,command=change)
# p2.add_radiobutton(label='50',variable=var,value=0.5,command=change)
# p2.add_radiobutton(label='60',variable=var,value=0.6,command=change)
# p2.add_radiobutton(label='70',variable=var,value=0.7,command=change)
# p2.add_radiobutton(label='80',variable=var,value=0.8,command=change)
p3.add_radiobutton(label='Pink',variable=var1,value=0,command=col)
p3.add_radiobutton(label='Green',variable=var1,value=2,command=col)
p3.add_radiobutton(label='White',variable=var1,value=1,command=col)
p4.add_command(label='Start',command=start_rec)
p4.add_command(label='Stop',command=stop_rec)
can=Canvas(win,bg='pink',height=600,width=950,cursor="plus red")
can.create_rectangle(0,0,950,600,fill='light blue',outline=colour,width=40)
can.grid(row=1,column=1,sticky = N + E + S + W)
...
win.config(menu=m1)
...
win.bind('<Control-s>',take_scr)
win.bind('<=>',h_inc)
win.bind('<minus>',h_dec)
win.bind('<.>',w_inc)
win.bind('<,>',w_dec)
win.bind('<Up>',up)
win.bind('<Down>',down)
win.bind('<Left>',left)
win.bind('<Right>',right)
win.bind("<MouseWheel>",zoomer)
win.bind("<Control-MouseWheel>",zoomer_ctrl)
win.bind('<Button-1>', SaveLastClickPos)
win.bind('<B1-Motion>', Dragging)
...
win.mainloop()
