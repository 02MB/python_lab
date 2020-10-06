squres = []
for values in range(1,11):
    squre = values**2
    squres.append(squre)
    print(squres)
print(squres)

squres = []
for values in range(1,11):
    squres.append(values**2)
    print(squres)
print(squres)

# digits = [1,2,3,4,5,6,7,8,9,0]
number_list = []
for numbers_list in range(0,10):
    number_list.append(numbers_list)
print(number_list)
print("min: " + str(min(number_list)))
print("max: " + str(max(number_list)))
print("sum: " + str(sum(number_list)))

squares = [value**2 for value in range(1,11)]
print(squares)