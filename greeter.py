# name = input("Please enter your name: ")
# print("Hello, " + name + "!")

# promt = 'If you tell us who you are, we can personalize the messages you see.'
# promt += "\nWaht is your first name? "

# name = input(promt)
# print("n\Hello, " + name + "!")

# age = input("How old are you? ")
# age = int(age)
# if age >= 18:
#     print("age >= 18")
# else:
#     print("Эмалолетка")

# def great_user(username, username_2):
#     print("hello, " + username.title() + "! " + username_2.title())


# great_user('maaaaax', 'dfddfdf')
# username = input('\nВведите имя 1: ')
# username_2 = input('\nВведите имя 2: ')
# great_user(username, username_2)

def get_formatted_name(first_name, last_name):
    full_name = first_name + ' ' + last_name
    return full_name.title()


while True:
    print("\nPlease tell me your name:")
    f_name = input("First name: ")
    l_name = input("Last name: ")

    formatted_name = get_formatted_name(f_name, l_name)
    print("\nHello, " + formatted_name + "!")