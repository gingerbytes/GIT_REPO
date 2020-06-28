from tkinter import Tk, Canvas, Button, Frame
from tkinter.filedialog import asksaveasfilename
from PIL import Image, ImageDraw

imgwidth = 800
imgheight = 300

tk = Tk()
tk.resizable(width=False, height=False)
cvs = Canvas(tk, width=imgwidth, height=imgheight)
cvs.pack()

#  4th value in the color parameter is the value of the alpha channel.
#  This sets the PNG to have transparent background
img = Image.new('RGBA', (imgwidth, imgheight), (255, 0, 0, 0))
draw = ImageDraw.Draw(img)

mousePressed = False
last = None


def press(evt):
    global mousePressed
    mousePressed = True


def release(evt):
    global mousePressed
    mousePressed = False


cvs.bind_all('<ButtonPress-1>', press)
cvs.bind_all('<ButtonRelease-1>', release)


def finish():
    # On button save click, save the signature as PNG.
    signature = asksaveasfilename(defaultextension=".png", title="Save Signature as PNG file.",
                                  confirmoverwrite=True, filetypes=(("PNG files", "*.png"), ("all files", "*.*")))
    img.save(signature)
    tk.destroy()


title_bar = Frame(tk, bg='black', relief='raised', bd=2)
savebutton = Button(title_bar, text='SAVE', command=finish)
title_bar.pack(expand=5)
savebutton.pack()


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


cvs.bind_all('<Motion>', move)
tk.mainloop()
