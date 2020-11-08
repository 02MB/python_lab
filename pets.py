pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')
print(pets)

print("\n\n\n\n\n\n")


def describe_pet(animal_type, pet_name):
    print("\nI have a " + animal_type + '.')
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
    print("\n")


describe_pet('Хищник', "милена")
describe_pet('dog', "willie")
describe_pet(animal_type='fdfdfdfd', pet_name='fffdddddfdfdfd')
describe_pet(pet_name='fffdddddfdfdfd', animal_type='fdfdfdfd')


def describe_pet(pet_name, animal_type='dog'):
    print("\nI have a " + animal_type + '.')
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
    print("\n")

describe_pet('бобик')
describe_pet('бобик', 'ff')


