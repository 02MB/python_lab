import time
from datetime import timedelta
import os

'''
Усложненный скрипт для чтения файла, с дополнительными условиями (if)
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
'''
s = {
            "Номер счета": {
                "ФИО": значение,
                "Остаток на счете": значение,
                "Дата операции": ['тип операции', сумма]
                }
}
'''


s = {}
f = open('text_01_01.txt', 'r', encoding='utf-8')
line = f.readline()

while line:
    if line[0:3] != 'OOO':
        a = line[0:11]  # номер счета
        b = line[11:41]  # ФИО
        c = line[41:47]  # остаток на счете
        # print("\t" + line[0:3])
        # print("\nAAAA" + " " + a)
        # print("\nAAAA" + " " + b)
        # print("\nAAAA" + " " + c)
        s[a] = {
            'FIO': b,
            'BANK': c,
            "DATA": {}
        }
    else:
        d = line[3:13]  # дата операции
        i = line[16:19]  # тип операции
        j = line[22:26]  # сумма по операции
        # print("\nBBBB" + " " + d)
        # print("\nBBBB" + " " + i)
        # print("\nBBBB" + " " + j)
        s[a]['DATA'][d] = [i, j]
        # for xxx, yyy in s.items():
        #     yyy['DATA'][d] = [i, j]
            # print("\n\t" + a)
            # print(d)
            # print(xxx)
            # s[a] = {
            #     # 'FIO': b,
            #     # 'BANK': c,
            #     'DATA': d  # : [i, j]
            # }
    line = f.readline()
    f.close
print(s)
for xx, yy in s.items():
    print("\nНомер счета: " + xx)
    print("\tФИО: " + yy['FIO'])
    print("\tДАТА: " + str(yy['DATA']))


end_time = time.monotonic()
print("\nЗатраченное время на скрипт: ")
print(timedelta(seconds=end_time-start_time))
