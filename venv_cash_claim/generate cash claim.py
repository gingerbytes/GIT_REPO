from tkinter import *
from tkinter.filedialog import askdirectory

tk = Tk()
tk.withdraw()  # hides tk dialog box.

path = askdirectory()
print(path)
