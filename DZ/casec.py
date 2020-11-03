# Тут будет Домашнии задания из книги: Изучаем Python программирование
'''
# 2-3
name_user = 'Maksim Petrovich'
print("Hello " + name_user + ", would like to learm Python today?")
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
# 2-4
name_user = 'MAksim petRovich'
print(name_user.upper())
print(name_user.lower())
print(name_user.title())
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
# 2-5
print("Albert Einstein once said,\n\"A person who never made a mistake never tried anything new\"")
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
# 2-6
famous_person = "Albert Einstein"
message = 'once said,\n\"A person who never made a mistake never tried anything new\"'
print(famous_person + message)
print("\n\n\n\n\n\n\n\n\n\n\n")
# 2-7
name_user = ' Name User '
print("!" + name_user + "!" + "\n\t!" + name_user.lstrip() + "!" +
      "\n\t!" + name_user.rstrip() + "!" + "\n\t!" + name_user.strip() + "!")
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
# 2-8
print(5+3)
print(10-2)
print(2 * 4)
print(16 / 2)
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
# 2-9
my_number = 29
print("My number " + str(my_number) + " !")
# 3-1
name_list = ["Вася", "Петя", "Лошарик"]
print(name_list)
print(name_list[0])
print(name_list[1])
print(name_list[2])
# 3-2
print("Я не дружу с " + name_list[0])
print("Я не дружу с " + name_list[1])
print("Я не дружу с " + name_list[2])
# 3-3
car_list = ['mazda', 'bmv', 'kamaz']
message = 'Я куплю себе машину, марки: '
print(message + car_list[2].title())
# 3-4
name_list = ["oleg", "alex", "max"]
print("Приглашаю тебя " + name_list[0].title() + " на обед!")
print("Приглашаю тебя " + name_list[1].title() + " на обед!")
print("Приглашаю тебя " + name_list[2].title() + " на обед!")
print("К сожалению не сможет прийти на обед: " + name_list.pop().title())
print(name_list)
name_list.append('Masha')
print(name_list)
print("Приглашаю тебя " + name_list[0].title() + " на обед!")
print("Приглашаю тебя " + name_list[1].title() + " на обед!")
print("Приглашаю тебя " + name_list[2].title() + " на обед!")
# 3-6
name_list.insert(0, "pasha")
name_list.insert(2, "olga")
name_list.append("vasya")
print(name_list)
print("Приглашаю тебя " + name_list[0].title() + " на обед!")
print("Приглашаю тебя " + name_list[1].title() + " на обед!")
print("Приглашаю тебя " + name_list[2].title() + " на обед!")
print("Приглашаю тебя " + name_list[3].title() + " на обед!")
print("Приглашаю тебя " + name_list[4].title() + " на обед!")
print("Приглашаю тебя " + name_list[5].title() + " на обед!")
# 3-7
print("На обед приглашаются всего два гостя " + str(name_list))
print("Мы сожалеем что Вы не сможете прийти " + name_list.pop().title())
print("Мы сожалеем что Вы не сможете прийти " + name_list.pop().title())
print("Мы сожалеем что Вы не сможете прийти " + name_list.pop().title())
print("Мы сожалеем что Вы не сможете прийти " + name_list.pop().title())
print("Для Вас приглашение действительно " + name_list[0].title())
print("Для Вас приглашение действительно " + name_list[1].title())
del name_list[0]
del name_list[0]
print(name_list)
# 3-8
country = ["Россия", "США", "Южная Корея", "Япония", "Канада", "Аргентина"]
print("Оригинальный список")
print(country)
print("Сортировка в Алфовитном порядке")
print(sorted(country))
print("Оригинальный список")
print(country)
print("Сортировка в обратном порядке")
print(sorted(country, reverse=True))
print("Оригинальный список")
print(country)
country.reverse()
print("reverse #1")
print(country)
country.reverse()
print("reverse #2")
print(country)
country.sort()
print("sort #1")
print(country)
country.sort()
print("sort #2")
print(country)
# 3-9
# тут будет ноль, т.к. там список пустой после удаления элементов списка
print(len(name_list))
# 3-10
list_310 = ["Ямайка", "Россия", "США", "Аргентина", "Япония", "Биробиджан"]
print("\n\n\n\n\n\n\n\n\n\n\n\n\n")
print(list_310)
print(len(list_310))
list_310.sort()
print(list_310)
list_310.sort(reverse=True)
print(list_310)
print(sorted(list_310))
print(list_310)
print(list_310.pop())
print(list_310)
del list_310[2]
print(list_310)
print(list_310[0])
list_310.append("fgfg")
list_310.insert(0, "fff")
print(list_310)
# 4-1
print("\n\n\n\n\n\n\n\n\n")
pizza_list = ['pizza_1', 'pizza_2', 'pizza_3']
for pizza in pizza_list:
    print(pizza)
for pizza in pizza_list:
    print("I like pepperoni pizza " + pizza.title())
print("I realy love pizza!")
# 4-2
pets = ['cat', 'dog', 'mouse']
for pet in pets:
    print(pet)
    print("A dog would make a great pet " + pet)
print("Any of these animals would make a great pet!")

print("\n\n\n\n\n\n\n\n\n")
# 4-3
a = range(1, 21)
for b in a:
    print("Число: " + str(b))
# 4-4
# a = range(1,1000000)
# for b in a:
#     print("Число: " +str(b))
# 4-5
a = range(1, 1000001)
print("min число в 1 000 000 это: " + str(min(a)))
print("max число в 1 000 000 это: " + str(max(a)))
print("сумма чисел 1 000 000 это: " + str(sum(a)))
# 4-6
a = range(1, 21, 2)
for b in a:
    print("нечетные числа диапозона 1-20: " + str(b))
# 4-7
a = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]
for b in a:
    print(b)
print(a)
# 4-8
a = range(1, 11)
for b in a:
    print(b**3)
# 4-9
a = [b**3 for b in range(1, 11)]
print(a)
# 4-10
my_foods = ['pizza', 'falafel', 'carrot cake', 'cannoli', 'ice cream', 'tea']
print("The first  three items in the list are: ")
print(my_foods[0:3])
print("Three items from the middle of the list are: ")
print(my_foods[3:5])
print("The last three items in the list are:")
print(my_foods[-3:])
# 4-11
my_pizza = ['pizza-1', 'pizza-2', 'pizza-3', 'pizza-4']
friend_pizza = my_pizza[:]
my_pizza.append('pizza-5')
friend_pizza.append('pizza-6')
print("My favorite pizzas are:")
for my in my_pizza:
    print(my)
print("My friend's favorite pizzas are:")
for friend in friend_pizza:
    print(friend)
# 4-12
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
for my in my_foods:
    print(my)
for friend in friend_foods:
    print(friend)
# 4-13
bludo = ('eda 1', 'eda 2', 'eda 3', 'eda 4', 'eda 5')
for eda in bludo:
    print("В меню ресторана входят блюда:")
    print(eda)
bludo = ('eda 1', 'eda 2', 'eda 3', 'eda 4', 'eda 5', 'eda 6', 'eda 7')
for eda in bludo:
    print("В обновленное меню ресторана входят следующие блюда")
    print(eda)
# 5-1
car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')

a = 100
print(a)
print('a => 100')
print(a >= 100)
print('a => 78')
print(a >= 78)
print('a => 50')
print(a >= 50)
print('a => 1')
print(a >= 1)
print('a => 99')
print(a >= 99)
print('a => 123')
print(a >= 123)
print('a => 1243')
print(a >= 1243)
print('a => 14243')
print(a >= 14243)
print('a => 101')
print(a >= 101)
# 5-2
# conditional_test.py
# 5-3
alien_color = 'red'
if 'green' in alien_color:
    print("Вы заработали: " + str(5) + " очков!")
else:
    print("Вы не заработали очки!")
# 5-4
alien_color = 'red'
if "green" in alien_color:
    a = 5
else:
    a = 10
print("Вы заработали: " + str(a) + " очков!")
# 5-5
alien_color = "1"
b = 0
if 'green' in alien_color:
    b = 5
elif "yellow" in alien_color:
    b = 10
elif "red" in alien_color:
    b = 15

print("ВЫЫЫ заработали: " + str(b) + " очков!")
# 5-6
age = 65
if age < 2:
    text = "младенец"
elif 4 > age >= 2:
    text = "малыш"
elif 13 > age >= 4:
    text = "ребенок"
elif 20 > age >= 13:
    text = "подросток"
elif 65 > age >= 20:
    text = "взрослый"
elif age >= 65:
    text = "пожилой человек"
print("Вы: " + text)
# 5-7
favorite_fruits = ["fruits_1", "fruits_2", "fruits_3", "fruits_4", "fruits_5"]
if "fruits_01" in favorite_fruits:
    print("You really like bananas!")
if "fruits_1" in favorite_fruits:
    print("You really like fruits_1")

# 6-1
human = {'first_name': 'Max', 'last_name': 'Miko', 'age': 21, 'city': 'KHV'}
print(human)
# 6-2
number = {'olga': 1, 'sara': 2, 'max': 3, 'sasha': 4, "pasha": 5}
print("Любимое число Ольги: " + str(number['olga']))
print("Любимое число sara: " + str(number['sara']))
print("Любимое число max: " + str(number['max']))
print("Любимое число sasha: " + str(number['sasha']))
print("Любимое число pasha: " + str(number['pasha']))
# 6-3
text = {'aaa': 'aaaa aaaa aaaaaaaaaa aaaaaaaa aaaa',
        'bbb': 'bb bbbb b bbbbb bbbbbbbb b', 'ccc': 'cccc cc ccccc cccc c'}
print('\n\n\nAAA: ' + text['aaa'])
print('\n\n\nBBB: ' + text['bbb'])
print('\n\n\nCCC: ' + text['ccc'])
# 6-4
text = {'aaa': 'aaaa aaaa aaaaaaaaaa aaaaaaaa aaaa',
        'bbb': 'bb bbbb b bbbbb bbbbbbbb b', 'ccc': 'cccc cc ccccc cccc c'}
for a, b in text.items():
    print(a + " это " + b)

# 6-5
slovari = {'Река 1': 'Страна 1', "Река 2": 'Страна 2', "Река 3": 'Страна 3'}
for a, b in slovari.items():
    print("Река: " + a.title() + " протекает в стране: " + b.title())
for a in slovari.keys():
    print("Реки: " + a.title())
for a in slovari.values():
    print("Страны: " + a.title())
# 6-6
favorite_languages = {
    'max': 'python',
    'olga': 'c',
    'sabina': 'Java',
    'oleg': 'Pascal',
    'lena': 'c'
}
name_01 = ['oleg', 'max', 'pasha', 'milena']
for user in favorite_languages.keys():
    if user in name_01:
        print(user.title() + ", спасибо за участие в опросе!")
    else:
        print(user.title() + ", Вам необходимо принять участие в опросе!")

# 6-7
human_01 = {'first_name': 'Max', 'last_name': 'Miko', 'age': 21, 'city': 'KHV'}
human_02 = {'first_name': 'вывыax',
            'last_name': 'Mвывo', 'age': 221, 'city': 'KыHV'}
human_03 = {'first_name': 'Maпx',
            'last_name': 'Mikааo', 'age': 221, 'city': 'KHVи'}
people = [human_01, human_02, human_03]
print(people)
for aaa in people:
    print('First name: ' + aaa['first_name'])
    print('Last_name: ' + aaa['last_name'])
    print('Age: ' + str(aaa['age']))
    print('City: ' + aaa['city'])
    print("\n")
# 6-8 = 6-7
# 6-9
favorite_places = {
    'place_1': ['jon', 'olga'],
    'place_2': ['max'],
    'place_3': ['max', 'jon']
}
for aaa, bbb in favorite_places.items():
    print(str(bbb) + " " + str(aaa))
# 6-10
number = {'olga': [1, 2, 3], 'sara': [3, 3, 4], 'max': [
    3, 3, 4, 5, 6], 'sasha': [4, 4, 4, 56], "pasha": [5, 5, 5, 66, 6]}
print("Любимые числа Ольги: " + str(number['olga']))
print("Любимые числа sara: " + str(number['sara']))
print("Любимые числа max: " + str(number['max']))
print("Любимые числа sasha: " + str(number['sasha']))
print("Любимые числа pasha: " + str(number['pasha']))
# 6-11
cities = {
    'citi_01': {
        'contry': 'aaaa',
        'population': 'bbb',
        'fact': 'ccc',
    },
    'citi_02': {
        'contry': 'aaaa2',
        'population': 'bbb2',
        'fact': 'ccc2',
    },
    'citi_03': {
        'contry': 'aaaa3',
        'population': 'bbb3',
        'fact': 'ccc3',
    }
}
print(cities)
for a, b in cities.items():
    print("\nГород: " + str(a).title())
    print("\tЭтот город надохидся в стране: " + b['contry'])
    print("\tНаселение составляет: " + b['population'])
    print("\tИнтересный факт: " + b['fact'])
# 7-1
car = input("You car? ")
print('Let me see if I can find you a ' + car)
# 7-2
stol = input("На сколько человек Вы хотите заказать столик? ")
stol = int(stol)
if stol > 8:
    print("У Вас большой заказа, придется немного подождать")
else:
    print("Ваш столик готов!")

# тут тройные ковычки это комментарий целого блока


# 7-3
number = input("Введите число кратное 10. Ваше число: ")
number = int(number)

if number % 10 == 0:
    print("Ваше число кратное!")
else:
    print("Ваше число не кратное!")


# 7-4
text = ("\nУкажите какое дополнение к пицце Вы хотите: ")
text += ("\t\nДля выхода введите 'stop' ")
message = ''
while message != 'stop':
    message = input(text)
    print(message + ", добавлено в заказ!")

'''
# 7-5
text = ("\n\tУкажите Ваш возрат: ")

a = "Бесплатно"
b = "$10"
c = "$15"
flag = True
while flag:
    # while True:
    x = input(text)
    x = int(x)
    if x <= 3:
        print("Цена билета составляет: " + a)
        # break
        flag = False
    elif 3 <= x <= 12:
        print("Цена билета составляет: " + b)
        # break
        flag = False
    elif x >= 12:
        print("Цена билета составляет: " + c)
        # break
        flag = False
