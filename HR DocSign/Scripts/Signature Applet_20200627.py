# from tkinter import Tk, Canvas, Button, Frame
from tkinter import *
from tkinter.filedialog import asksaveasfilename
from PIL import Image, ImageDraw


def press(evt):
    global mousePressed
    mousePressed = True


def release(evt):
    global mousePressed
    mousePressed = False


def finish():
    # On button save click, save the signature as PNG.
    signature = asksaveasfilename(defaultextension=".png", title="Save Signature as PNG file.",
                                  confirmoverwrite=True, filetypes=(("PNG files", "*.png"), ("all files", "*.*")))
    img.save(signature)
    tk.destroy()


def move(evt):
    # captures the actual mouse movement.
    global mousePressed, last
    x, y = evt.x, evt.y
    if mousePressed:
        if last is None:
            last = (x, y)
            return
        draw.line(((x, y), last), (0, 0, 0), width=3)
        cvs.create_line(x, y, last[0], last[1], width=3)
        last = (x, y)
    else:
        last = (x, y)


imgwidth = 800
imgheight = 300
padding = 20

tk = Tk()
tk.resizable(width=False, height=False)
tk.overrideredirect(True)  # turns off default tk title bar and window.
# tk.geometry(f'{imgwidth}x{imgheight}')  # set new window.
tk.configure(bg='red')

# set custom title bar and buttons.
# tkinter use X as a global variable, thus you need to import * from tkinter
title_bar = Frame(tk, height=35, bg='red', relief='raised', bd=0)
title_bar.pack(expand=1, fill=X, side=TOP)
#title_bar.place(x=0, y=0, height=imgwidth+padding, width=imgheight+padding+40)

cvs = Canvas(tk, width=imgwidth - padding, height=imgheight - padding)
cvs.pack()
# cvs.place(x=10, y=50, width=imgwidth - padding, height = imgheight - padding - 50)

#  4th value in the color parameter is the value of the alpha channel.
#  This sets the PNG to have transparent background
img = Image.new('RGBA', (imgwidth, imgheight), (255, 0, 0, 0))
draw = ImageDraw.Draw(img)

# use place() for buttons to control position.
#clearbutton = Button(title_bar, text='CLEAR', command=clearsig)
savebutton = Button(title_bar, text='SAVE', command=finish)
closebutton = Button(title_bar, text='CLOSE', command=tk.destroy)
#clearbutton.place(x=205, y=5, height=25, width=100)
savebutton.place(x=310, y=5, height=25, width=100)
closebutton.place(x=415, y=5, height=25, width=100)

mousePressed = False
last = None

cvs.bind_all('<ButtonPress-1>', press)
cvs.bind_all('<ButtonRelease-1>', release)

cvs.bind_all('<Motion>', move)
tk.mainloop()
