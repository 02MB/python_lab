# 5-8
user_names = ['max', 'olga', 'admin', 'sabina', 'jon']

for user_name in user_names:
    if user_name == 'admin':
        print('Hello ' + user_name.title() +
              ', would you like to see a status report?')
    else:
        print("Hello " + user_name.title() +
              ', thank you for logging in again.')
# 5-9
user_names = ['d']

if user_names:
    print("User yes")
else:
    print("We need to find some users!")
for user_name in user_names:
    if user_name == 'admin':
        print('Hello ' + user_name.title() +
              ', would you like to see a status report?')
    else:
        print("Hello " + user_name.title() +
              ', thank you for logging in again.')
# 5-10
print("\n\n\n\n\n\n\n\n")

current_users = ['olga', 'max', 'jon', 'sabina', 'oleg', 'pasha']
new_users = ['olga', 'sabina', 'max', 'molli']

for new_user in new_users:
    if new_user in current_users:
        print(new_user.title() + " данное имя занято!")
    else:
        print(new_user.title() + " данное имя свободное!")

print("\n\n\n\n\n\n\n\n")

current_users = ['olga', 'Max', 'jon', 'sabina', 'oleg', 'pasha']
new_users = ['olga', 'sabina', 'mAx', 'molli']

for new_user in new_users:
    if new_user.lower() in str(current_users).lower():
        print(new_user + " данное имя занято!")
    else:
        print(new_user + " данное имя свободное!")

# 5-11
print("\n\n\n\n\n\n\n\n")

number_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
for a in number_list:
    print("Число: " + str(a))


number_list = range(1, 10)
abc = ['st', 'nd', 'rd', 'th']

for a in number_list:
    if a == 1:
        print(str(a) + str(abc[0]))
    elif a == 2:
        print(str(a) + str(abc[1]))
    elif a == 3:
        print(str(a) + str(abc[2]))
    elif a >= 4:
        print(str(a) + str(abc[3]))
