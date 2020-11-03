'''
message = input("Tell me something, and I will repeat it back to you: ")
print(message)

promt = "\nTell me something, and I will repeat it back to you:"
promt += "\nEnter 'quit' to end the program. "
message = ""
while message != "quit":
    message = input(promt)
    if message != 'quit':
        print(message)

'''

promt = "\nTell me something, and I will repeat it back to you:"
promt += "\nEnter 'quit' to end the program. "

flag = True
message = ""
while flag:
    message = input(promt)

    if message == 'quit':
        flag = False
    else:
        print(message)
