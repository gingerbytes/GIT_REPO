from tkinter import *
from tkinter.filedialog import askopenfilename
from openpyxl import load_workbook
# import xlrd

ws_name = 'Details'  # this worksheet contains the employee details.

tk = Tk()
tk.withdraw()  # hides tk dialog box.
# EE_list = askopenfilename(title="Open EE List Excel File.", filetypes=(("xlsx files", "*.xlsx"), ("all files", "*.*")))
# print(EE_list)
EE_list = 'C:/Users/gdangca/OneDrive - Infor/Projects/Project - Python/GIT_REPO/venv_authority_to_deduct/Files/EE List 06-19-2020 nosal.xlsx'

wb = load_workbook(EE_list, read_only=True)
for i in range(len(wb.sheetnames)):
    if wb.sheetnames[i] == ws_name:
        wb.active = i
        break
else:
    print(f'{ws_name} worksheet is not in the excel file. try another file')

while True:
    emp_id = input("Please input employee ID of applicant: ")
    if emp_id.isdigit():
        break

# wb = openpyxl.load_workbook(filepath)
# ws = wb.active
# cell_obj = ws.cell(row = 2, column = 11)
# print(cell_obj.value)

# XLRD
# book = xlrd.open_workbook(filepath)
# first_sheet = book.sheet_by_index(0)
# cell = first_sheet.cell(2, 11)
# print(cell)
# print(cell.values)
