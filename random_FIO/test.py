'''
text = ['Александр\n', 'Дмитрий\n', 'Максим\n']
# text = 'Александр\n'
print(text)
# print(text.rstrip("\n"))
# text = text.rstrip("\n")
text2 = []

for x in text:
    print(x)
    y = x.rstrip('\n')
    text2.append(y)

print("\tnew" + " " + str(text))
print("\n" + str(text2))
'''
# test = {
#     'user0': ['Давыдов', 'Николай', 'Иосифович'],
#     'user1': ['Волков', 'Георгий', 'Платонович'],
#     'user2': ['Егоров', 'Богдан', 'Валентинович'],
#     'user3': ['Абрамов', 'Валерий', 'Степанович'],
#     'user4': ['Игнатьев', 'Влад', 'Георгиевич'],
#     'user5': ['Семёнов', 'Даниэль', 'Геннадиевич'],
#     'user6': ['Волков', 'Георгий', 'Платонович'],
# }
test = {
    'user0': 1,
    'user1': 2,
    'user2': 1
}

# for data in test.values():
#     if data == test:
#         print(" Есть совпадения! ")
#     else:
#         print("Совпадений нет! ")

for x, y in test.items():
    if y == test.values():
        print(" Есть совпадения! ")
    else:
        print("Совпадений нет! ")


# if test.values() == test.values():
#     print(" Есть совпадения! ")
# else:
#     print("Совпадений нет! ")
