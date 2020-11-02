import os
print(os.name)

print(os.getcwd())
os.chdir(r"D:\python_lab\file_test")
print(os.getcwd())
# for aaa in range(3):
#     os.mkdir("name_dir_"+str(aaa))
if os.path.exists('text1.txt') and os.path.exists('text2.txt') == True:
    # print(os.path.exists('text1.txt'))
    print("Файлы *.txt существуют")
else:
    print("Файлы *.txt НЕ существуют")
with open('text1.txt', 'r') as file:
    print(file.read())
