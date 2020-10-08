# Тут будет Домашнии задания из книги: Изучаем Python программирование

#2-3
name_user = 'Maksim Petrovich'
print("Hello " + name_user + ", would like to learm Python today?")
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
#2-4
name_user = 'MAksim petRovich'
print(name_user.upper())
print(name_user.lower())
print(name_user.title())
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
#2-5
print("Albert Einstein once said,\n\"A person who never made a mistake never tried anything new\"")
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
#2-6
famous_person = "Albert Einstein"
message = 'once said,\n\"A person who never made a mistake never tried anything new\"'
print(famous_person + message)
print("\n\n\n\n\n\n\n\n\n\n\n")
#2-7
name_user = ' Name User '
print("!" + name_user + "!" + "\n\t!" + name_user.lstrip() + "!" + "\n\t!" + name_user.rstrip() + "!" + "\n\t!" + name_user.strip() + "!")
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
#2-8
print(5+3)
print(10-2)
print(2 * 4)
print(16 / 2)
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
#2-9
my_number = 29
print("My number " + str(my_number) + " !")
#3-1
name_list = ["Вася", "Петя", "Лошарик"]
print(name_list)
print(name_list[0])
print(name_list[1])
print(name_list[2])
#3-2
print("Я не дружу с " + name_list[0])
print("Я не дружу с " + name_list[1])
print("Я не дружу с " + name_list[2])
#3-3
car_list = ['mazda', 'bmv', 'kamaz']
message = 'Я куплю себе машину, марки: '
print(message + car_list[2].title())
#3-4
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
#3-6
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
#3-7
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
#3-8
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
#3-9
print(len(name_list)) #тут будет ноль, т.к. там список пустой после удаления элементов списка
#3-10
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
#4-1
print("\n\n\n\n\n\n\n\n\n")
pizza_list = ['pizza_1', 'pizza_2', 'pizza_3']
for pizza in pizza_list:
    print(pizza)
for pizza in pizza_list:
    print("I like pepperoni pizza "+ pizza.title())
print("I realy love pizza!")
#4-2
pets = ['cat', 'dog', 'mouse']
for pet in pets:
    print(pet)
    print("A dog would make a great pet " + pet)
print("Any of these animals would make a great pet!")

print("\n\n\n\n\n\n\n\n\n")
#4-3
a = range(1,21)
for b in a:
    print("Число: " +str(b))
#4-4
# a = range(1,1000000)
# for b in a:
#     print("Число: " +str(b))
#4-5
a = range(1,1000001)
print("min число в 1 000 000 это: " + str(min(a)))
print("max число в 1 000 000 это: " + str(max(a)))
print("сумма чисел 1 000 000 это: " + str(sum(a)))
#4-6
a = range(1, 21, 2)
for b in a:
    print("нечетные числа диапозона 1-20: " + str(b))
#4-7
a = [3,6,9,12,15,18,21,24,27,30]
for b in a:
    print(b)
print(a)
#4-8
a = range(1,11)
for b in a:
    print(b**3)
#4-9
a = [b**3 for b in range(1,11)]
print(a)
#4-10
my_foods = ['pizza', 'falafel', 'carrot cake', 'cannoli', 'ice cream', 'tea']
print("The first  three items in the list are: ")
print(my_foods[0:3])
print("Three items from the middle of the list are: ")
print(my_foods[3:5])
print("The last three items in the list are:")
print(my_foods[-3:])
#4-11
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
#4-12
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
for my in my_foods:
    print(my)
for friend in friend_foods:
    print(friend)
#4-13
bludo = ('eda 1','eda 2','eda 3','eda 4','eda 5')
for eda in bludo:
    print("В меню ресторана входят блюда:")
    print(eda)
bludo = ('eda 1','eda 2','eda 3','eda 4','eda 5', 'eda 6', 'eda 7')
for eda in bludo:
    print("В обновленное меню ресторана входят следующие блюда")
    print(eda)
#5-1
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
#5-2
# conditional_test.py
