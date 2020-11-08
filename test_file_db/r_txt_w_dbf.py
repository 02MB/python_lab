# Читаем txt и записываем в dbf файл
import dbf
import os
import sys

os.chdir(r"D:\python_lab\test_file_db")


'''
# Пример из Интернета - рабочий!
table = dbf.Table('test.dbf', 'cod N(1,0); name C(30)')
table.open(mode=dbf.READ_WRITE)
for x in range(0, 10):
    row_tuple = (str(int(x)), "name" + str(int(x)))
    table.append(row_tuple)
table.close
'''
# s = {'ФИО': [номер счета, сумма на счете]}
s = {}

f = open('text_01.txt', 'r', encoding='utf-8')
line = f.readline()

while line:
    # print(line)
    # print("\nНомер счета: " + line[0:11])
    # print("\tФИО владельца счета: " + line[11:41])
    # print("\tСумма на счете: " + line[41:47])
    a = line[0:11]
    b = line[11:41]
    c = line[41:47]
    s[b.strip()] = [a, c]  # тут убираем все лишние пробелы вокруг ФИО
    # s[b] = [a, c]
    line = f.readline()
    f.close
# print(s)


table = dbf.Table(
    'test.dbf', 'fio C(47); numberbank N(11,0); money N(6,0)', codepage='utf8')
table.open(mode=dbf.READ_WRITE)
for x, y in s.items():
    row_tuple = (str(x), str(int(y[1])), str(int(y[0])))
    table.append(row_tuple)
table.close
