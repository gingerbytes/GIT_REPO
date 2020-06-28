from tkinter.filedialog import askopenfilename
from tkinter import Tk
import fitz


def PDF_addsignature(fname, newname, signpng):
    # fitz.Rect defined by four floating point numbers x0, y0, x1, y1.
    x0 = 90     # distance from left.
    y0 = 640    # distance from top.
    x1 = 250    # width of signature.
    y1 = 690    # height, affects vertical position.

    pos = fitz.Rect(x0, y0, x1, y1)
    f = fitz.open(fname)
    f_pageone = f[0]

    f_pageone.insertImage(pos, signpng, keep_proportion=True)
    f.save(newname)


# ask user to open PDF file and PNG file.
Tk().withdraw()
pdf_contract = askopenfilename(title="Open PDF contract file to sign.", filetypes=(
    ("PDF files", "*.pdf"), ("all files", "*.*")))
pdf_contract_signed = pdf_contract[:len(pdf_contract) - 4] + '_signed.pdf'

img_signature = askopenfilename(title="Now open your PNG signature file.", filetypes=(
    ("PNG files", "*.png"), ("all files", "*.*")))

PDF_addsignature(pdf_contract, pdf_contract_signed, img_signature)
