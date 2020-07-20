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


def PDF_addsignature(fname, newname, pdf):
    # fitz.Rect defined by four floating point numbers x0, y0, x1, y1.
    x0 = 330    # distance from left.
    y0 = 242    # distance from top.
    x1 = 490    # width of signature.
    y1 = 292    # height, affects vertical position.

    img_signature = askopenfilename(title="Now Open Your PNG Signature File.", filetypes=(
        ("PNG files", "*.png"), ("all files", "*.*")))

    pos = fitz.Rect(x0, y0, x1, y1)
    pdf.insertImage(pos, img_signature, keep_proportion=True)

def pdf_add_amount_term(fname, newname):
    # loan terms and coordinates in the page where to put the 'X'
    terms = {'6':(237, 141), '12':(237, 152),'18':(237, 165),'24':(237, 176),'36':(237, 188)}

    loan = input("Please input loan amount: PhP ")
    if ',' not in loan:
        loan = f'{int(loan):,}'

    while True:
        term = input("Please input loan term (6, 12, 18, 24, 36) months: ")
        if term in terms.keys():
            break

    loan_xy = fitz.Point(240, 117)
    doc = fitz.open(fname)
    page = doc[0]
    page.insertText(loan_xy, loan, rotate=0, fontsize=9, render_mode=0, overlay = True)
    page.insertText(terms[term], 'X', rotate=0, fontsize=9, render_mode=0, overlay = True)

    PDF_addsignature(fname, newname, page)
    doc.save(newname)
    startfile(newname)  # open the signed PDF.
    return

def popup_done(msg):
    popup = Tk()
    popup.wm_title("FINISHED!")
    label = ttk.Label(popup, text=msg)
    label.pack(side="top", fill="x", pady=10)
    B1 = ttk.Button(popup, text="CLOSE", command=popup.destroy)
    B1.pack()
    popup.mainloop()

# ask user to open PDF file and PNG file.
Tk().withdraw()
pdf_atd = askopenfilename(title="Open Authority to Deduct PDF File to Sign.", filetypes=(
    ("PDF files", "*.pdf"), ("all files", "*.*")))
pdf_atd_signed = pdf_atd[:len(pdf_atd) - 4] + '_Employee Signed.pdf'

pdf_add_amount_term(pdf_atd, pdf_atd_signed)
#popup_done(f'Success! Signed contract is saved at: \n{pdf_contract_signed}')

startfile(pdf_atd_signed)  # open the signed PDF.
