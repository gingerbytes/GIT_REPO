from tkinter import *
from tkinter.filedialog import askdirectory

tk = Tk()
tk.withdraw()  # hides tk dialog box.

# ask where the reports are located.
path = askdirectory()
print(path)
