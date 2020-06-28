from tkinter import Tk, Canvas, Button, Frame
from tkinter.filedialog import asksaveasfilename
from PIL import Image, ImageDraw

root = Tk()


def move_window(event):
    root.geometry('+{0}+{1}'.format(event.x_root, event.y_root))


root.overrideredirect(True)  # turns off title bar, geometry
root.geometry('400x100+200+200')  # set new geometry

# make a frame for the title bar
title_bar = Frame(root, bg='black', relief='raised', bd=2)

# put a close button on the title bar
close_button = Button(title_bar, text='CLOSE', command=root.destroy)

# a canvas for the main area of the window
window = Canvas(root, bg='black')

# pack the widgets
title_bar.pack(expand=5)
close_button.pack()
window.pack(expand=1)

# bind title bar motion to the move window function
title_bar.bind('<B1-Motion>', move_window)

root.mainloop()
