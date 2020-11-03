promt = "\nPlease enter the name of city you have visited:"
promt += "\n(Enter 'quit' when you are finished.)"

while True:
    city = input(promt)

    if city == "quit":
        break
    else:
        print("I'd love to go to " + city.title() + "!")
