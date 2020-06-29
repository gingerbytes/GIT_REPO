'''
Having problems installing Fitz?
- having traits error after running "pip install fitz"?
- download "traits‑6.1.0‑cp38‑cp38‑win_amd64.whl" from https://www.lfd.uci.edu/~gohlke/pythonlibs/
- cp38 means Python version 3.8
- pip install traits‑6.1.0‑cp38‑cp38‑win_amd64.whl
- pip install PyMuPDF
- pip install fitz
'''

from tkinter.filedialog import askopenfilename
from tkinter import Tk
from tkinter import ttk
import fitz
from os import startfile


def PDF_addsignature(fname, newname, signpng):
    # fitz.Rect defined by four floating point numbers x0, y0, x1, y1.
    x0 = 80     # distance from left.
    y0 = 540    # distance from top.
    x1 = 240    # width of signature.
    y1 = 590    # height, affects vertical position.

    pos = fitz.Rect(x0, y0, x1, y1)
    f = fitz.open(fname)
    f_pageone = f[0]

    f_pageone.insertImage(pos, signpng, keep_proportion=True)
    f.save(newname)


def popup_done(msg):
    popup = Tk()
    popup.wm_title("FINISHED!")
    label = ttk.Label(popup, text=msg)
    label.pack(side="top", fill="x", pady=10)
    B1 = ttk.Button(popup, text="CLOSE", command=popup.destroy)
    B1.pack()
    popup.mainloop()


# filter PDF file to select with correct filename.
filekeyword = 'Job Offer Sheet' + "*.pdf"
#filekeyword = "*.pdf"

# ask user to open PDF file and PNG file.
Tk().withdraw()
pdf_contract = askopenfilename(title="Open PDF Contract File to Sign.", filetypes=(
    ("PDF files", filekeyword), ("all files", "*.*")))
pdf_contract_signed = pdf_contract[:len(pdf_contract) - 4] + '_HR Signed.pdf'

img_signature = askopenfilename(title="Now Open Your PNG Signature File.", filetypes=(
    ("PNG files", "*.png"), ("all files", "*.*")))

PDF_addsignature(pdf_contract, pdf_contract_signed, img_signature)
#popup_done(f'Success! Signed contract is saved at: \n{pdf_contract_signed}')

startfile(pdf_contract_signed)  # open the signed PDF.
