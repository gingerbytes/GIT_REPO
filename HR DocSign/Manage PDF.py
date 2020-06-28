from PyPDF2 import PdfFileReader, PdfFileWriter


path = "C:\\Users\\gdangca\\OneDrive - Infor\\Projects\\Project - Python\\HR DocSign\\Files\\"
signature = path + "signature - gerard_02.png"
signaturePDF = path + "signature - gerard_02.pdf"
contract = path + "Sample contract.pdf"
contractsigned = contract[:len(contract) - 4] + '_signed.pdf'


def createPDF():
    file1 = canvas.Canvas("Statements.pdf", pagesize=letter)
    file1.drawString(100, 400, "HELLOOOO")
    file1.save()


def PDFpagewriter(fname, newname):
    # writing the PDF page to a new PDF file,  ONE PAGE
    # PyPDF2 does not support writing over the existing PDF file.
    f = open(fname, 'rb')
    pdf_reader = PdfFileReader(f)
    # print(pdf_reader.numPages)

    page_one = pdf_reader.getPage(0)
    page_one_text = page_one.extractText()
    # print(page_one_text)

    pdf_writer = PdfFileWriter()
    pdf_writer.addPage(page_one)
    pdf_output = open(newname, 'wb')
    pdf_writer.write(pdf_output)
    f.close()
    pdf_output.close()


def PDFbookwriter(fname, newname):
    # writing the PDF with multiple pages to a new PDF file.
    f = open(fname, 'rb')
    pdf_text = []

    pdf_reader = PdfFileReader(f)
    pdf_writer = PdfFileWriter()
    pdf_output = open(newname, 'wb')

    newpage = ['HELLO THIS IS A NEW PAGE']

    for num in range(pdf_reader.numPages):
        page = pdf_reader.getPage(num)
        # page type cast is PyPDF2.pdf.PageObject

        pdf_text.append(page.extractText())
        # print(f'--------------  PAGE {num + 1} --------------')
        # print(pdf_text[num])
        pdf_writer.addPage(page)

    pdf_writer.write(pdf_output)
    pdf_output.close()
    f.close()


def PDFwatermark(fname, newname, pdfsign):
    # writing the PDF with multiple pages to a new PDF file.

    pdf_reader = PdfFileReader(fname)
    pdf_writer = PdfFileWriter()
    pdf_watermark = PdfFileReader(pdfsign)
    # Read signature from page 1.
    pdf_watermark_page = pdf_watermark.getPage(0)

    for num in range(pdf_reader.numPages):
        page = pdf_reader.getPage(num)
        # page type cast is PyPDF2.pdf.PageObject
        page.mergePage(pdf_watermark_page)
        pdf_writer.addPage(page)

    with open(newname, 'wb') as out:
        pdf_writer.write(out)

    out.close()


def PDF_addsignature_pages():
    # !/usr/bin/python
    # Adding a watermark to a multi-page PDF

    input_file = "example.pdf"
    output_file = "example-drafted.pdf"
    watermark_file = "barcode.pdf"

    # define the reader and writer objects
    reader_input = PdfReader(input_file)
    writer_output = PdfWriter()
    watermark_input = PdfReader(watermark_file)
    watermark = watermark_input.pages[0]

   # go through the pages one after the next
   for current_page in range(len(reader_input.pages)):
        merger = PageMerge(reader_input.pages[current_page])
        merger.add(watermark).render()

    # write the modified content to disk
    writer_output.write(output_file, reader_input)

'''
What percent of X is Y?  % = Y / X
Example, X is 60, Y is 12, so the equation is 12/60 = (0.20 * 100) = 20%
So 12 is 20% of 60.

What is Z% of X?
Example Z = 10% of X = 150, find Y.
Y = Z * X;  Y = 10% * 150;  Y = 0.10 * 150;  Y = 15 .: So 10% of 150 is 15

'''


def resize_signature(sig, sigr):
    width = 0
    height = 0
    s_height = 200  # preferred signature height
    s_width = 0

    im = Image.open(sig)
    width, height = im.size

    # thumbnail is height, width.
    im.thumbnail((183, 431), Image.ANTIALIAS)
    im.save(sigr, 'PNG', quality=90)

    # put the signature in the PDF.
    PDF_addsignature(pdf_contract, pdf_contract_signed, sigr)

# PDFbookwriter(contract, contractsigned, signaturePDF)
# PDFwatermark(contract, contractsigned, signaturePDF)
