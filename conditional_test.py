car_1 = 'Audi'
car_2 = 'bmw'
car_3 = 'audi'
if car_1 != car_2:
    print("car_1 != car_2")
if car_1 == car_2:
    print("car_1 == car_2")
else:
    print("car_1 != car_2")
if car_1 == car_3:
    print("car_1 == car_3")
else:
    print("car_1 != car_3")
if car_1.lower() == car_3:
    print("car_1.lower() == car_3")

a = 10
b = 5
c = 11
print('\n\n\n\n\n\n')
print("a: " + str(a),"b: " + str(b),"c: " + str(c))
if a == b:
    print('a = b')
    print(a == b)
else:
    print('a != b')
    print(a != b)
if a == c:
    print('a = c')
    print(a == c)
if a > b:
    print("a > b")
    print(a > b)
if a < c:
    print("a < c")
    print(a < c)

if a and c >= b:
    print("a and c >= b")
    print(a and c >= b)
if a or b > c:
    print("a or b > c")
    print(a or b > c)

a = ['car_1', 'car_2', 'car_3']
if 'car_1' in a:
    print("car_1 yes")
if "car_4" not in a:
    print("car_4 not")

print("\n\n\n\n\n\n\n\n")
a = 3
b = 4
c = 3
print(a and b > c)
if a > c or b > c:
    print("fdfjd " + str(c))

