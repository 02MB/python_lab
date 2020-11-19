from openpyxl import Workbook
import random
import os
import sys
import openpyxl

# указываем наш основной каталог (где лежат файлы и т.д.)
os.chdir(r"D:\python_lab\random_FIO")

surname = []  # пустой список фамилий
name = []  # пустой список имен (использую только мужской род)
middle_name = []  # пустой список отчеств (использую только мужской род)
# описание словаря: {'userXXX':['surname', 'name', 'middle_name']}
dict_fio = {}


def openfile(name_file, name_list):
    f = open(name_file, 'r', encoding='utf-8')
    line = f.readline().split()
    while line:
        name_list.extend(line)
        line = f.readline().split()
    f.close


def random_fio(x):
    for i in range(x):
        dict_fio['user'+str(i)] = [random.choice(surname),
                                   random.choice(name), 
                                   random.choice(middle_name)]
    print(dict_fio)
    # тут бы не помешала проверка на дубликаты ФИО, если есть такие...


def excel():
    # Создаем Excel файл
    wb = Workbook()
    ws = wb.create_sheet('ФИО', 0)
    wb.active = 0
    row = 1
    wb.active["A"+str(row)] = 'Фамилия'
    wb.active["B"+str(row)] = 'Имя'
    wb.active["C"+str(row)] = 'Отчество'
    for x, y in dict_fio.items():
        row += 1
        wb.active["A"+str(row)] = y[0]
        wb.active["B"+str(row)] = y[1]
        wb.active["C"+str(row)] = y[2]
    wb.save('filename.xlsx')


openfile('name.txt', name)
openfile('surname.txt', surname)
openfile('middle_name', middle_name)
print(len(name))
print(len(surname))
print(len(middle_name))
print("Случайная фамилия: " + random.choice(surname))
print("Случайное имя: " + random.choice(name))
print("Случайное отчество: " + random.choice(middle_name))
random_fio(10)
excel()