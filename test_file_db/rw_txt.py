import time
from datetime import timedelta
import os

'''
Простой скрипт для чтения файла, без дополнительных условий (if)
Добавил счетчик времени - для анализа "timedelta"
0-11 номер счета
11-41 это ФИО
42-47 это сумма
'''
start_time = time.monotonic()
os.chdir(r"D:\python_lab\test_file_db")
if os.path.exists('text_01.txt') == True:
    print("Файл *.txt существует")
else:
    print("Файл *.txt НЕ существует")

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
    line = f.readline()
    f.close
print(s)

file_2 = open('text_02.txt', 'w', encoding='utf-8')
while file_2:
    for fio, info in s.items():
        file_2.write(fio + ' ' + info[0] + ' ' + info[1] + '\n')
    file_2.close
    break
end_time = time.monotonic()

# сохраняем в файл с кодировкой DOS
file_3 = open('text_02_02.txt', 'w', encoding='cp866')
while file_3:
    for fio, info in s.items():
        file_3.write(fio + ' ' + info[0] + ' ' + info[1] + '\n')
    file_3.close
    break
end_time = time.monotonic()
print("\nЗатраченное время на скрипт: ")
print(timedelta(seconds=end_time-start_time))
