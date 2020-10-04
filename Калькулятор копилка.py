# Если откладывать в неделю S, в течении Года, получим через год m.
s = 10
week = range(1, 55)
for m in week:
    print("Неделя №" + str(m))
    if m == 27:
        print("Прошло пол года")
    if m == 54:
        print("Прошел год")
    m = m * s
    print("Вы накопили: " + str(m))

# Вариант №2
print("\n\n\n\n\nВариант №2\n\n\n\n\n")
a = 10
c = 0
week = range(1, 55)
for b in week:
    if b == 27:
        print("Прошло пол года")
    if b == 54:
        print("Прошел год")
    # print("Прошлая неделя: " + str(c)) #Данный вывод просто для само проверки
    b = a + c
    c = b
    print("Текущая неделя: " + str(c))
