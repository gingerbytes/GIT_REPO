import PyPDF2

f1 = 'Job Offer Sheet - PSSC INFOR_2018.12.27.pdf'
f2 = f1[:len(f1) - 4] + '_edited.pdf'
f3 = 'HowTo Photoman.pdf'
f4 = f3[:len(f3) - 4] + '_edited.pdf'
signame = 'signature - gerard_02.png'


def PDFpagewriter(fname, newname):
    # writing the PDF page to a new PDF file.
    # PyPDF2 does not support writing over the existing PDF file.
    f = open(fname, 'rb')
    pdf_reader = PyPDF2.PdfFileReader(f)
    # print(pdf_reader.numPages)

    page_one = pdf_reader.getPage(0)
    page_one_text = page_one.extractText()
    # print(page_one_text)

    pdf_writer = PyPDF2.PdfFileWriter()
    pdf_writer.addPage(page_one)
    pdf_output = open(newname, 'wb')
    pdf_writer.write(pdf_output)
    f.close()
    pdf_output.close()


def PDFbookwriter(fname, newname):
    # writing the PDF pages to a new PDF file.
    f = open(fname, 'rb')
    pdf_text = []

    pdf_reader = PyPDF2.PdfFileReader(f)
    pdf_writer = PyPDF2.PdfFileWriter()
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


def createPDF():
    file1 = canvas.Canvas("Statements.pdf", pagesize=letter)
    file1.drawString(100, 400, "HELLOOOO")
    file1.save()


#PDFbookwriter(f3, f4)
createPDF()
