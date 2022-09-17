import csv
import os
from zipfile import ZipFile, ZIP_DEFLATED
from PyPDF2 import PdfReader
from openpyxl import load_workbook

# Task_1: Запаковать в zip архив несколько разных файлов: pdf, xlsx, csv
# Task_2: Положить его в ресурсы

target_path = './resources/'
source_path = './source'
file_dir = os.listdir(source_path)

with ZipFile(f'{target_path}file_4.zip', 'w', compression=ZIP_DEFLATED) as file_zip:
    for file in file_dir:
        add_file = os.path.join(source_path, file)
        file_zip.write(add_file, os.path.relpath(add_file, source_path))
    file_zip.extractall(target_path)

# Task_3: Реализовать чтение и проверку содержимого каждого файла из архива

print('CSV Check:')
with open(f'{target_path}file_3.csv') as file_csv:
    table = list(csv.reader(file_csv))
    for index, value in enumerate(table):
        if index == 11:
            print(value[4])
    assert 'Mara' == table[2][1]
    # for row in enumerate(table):
    #     print(row) # распечатать весь файл

print('\nXLSX Check:')
workbook = load_workbook(f'{target_path}file_2.xlsx')
sheet = workbook.active
print(sheet.cell(row=3, column=2).value)  # OR print(sheet['B3'].value)
assert sheet[23][1].value == 'Что нужно сделать, чтобы функция возвратила значение?'

print('\nPDF Check:')
pdf_reader = PdfReader(f'{target_path}file_1.pdf')
page = pdf_reader.pages[1]
text = page.extract_text()
print(text)
assert 'The end, and just as well' in text
