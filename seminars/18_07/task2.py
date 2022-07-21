# Найдите корни квадратного уравнения Ax^2 + Bx +C = 0 двумя способами:
#     1. с помощью математических формул нахождения корней квадратного уравнения
#     2. с помощью дополнительных библиотек Phyton
# 1. метод - Расчленение и математические формулы
# path = r'folder\task2.txt'
# with open (path,'r') as my_file:
#     data = my_file.read()

# data = data.split()
# print(data)
# data = data[:-2]
# print(data)
# data = [int(data[0][:-3]), int((data[1]+data[2])[:-1]), int(data[3] + data[4])]
# print(data)

# d = data[1]**2 - 4*data[0]*data[2]
# print(d)

# x_1 = (-data[1] + d**0.5)/(2*data[0])
# x_2 = (-data[1] - d**0.5)/(2*data[0])

# print(x_1, x_2)

# 2. метод - математич.формулы

import os
path = os.path.join('folder','task2_2.txt')

with open(path,'r') as data:
    a = int(data.readline())
    b = int(data.readline())
    c = int(data.readline())
print(a,b,c)

disc = b**2 - 4*a*c
x1 = -b + (disc**(1/2)/(2*a))
x2 = -b - (disc**(1/2)/(2*a))
print (round(x1,3), round(x2,3))

with open(path,'a') as data:
    data.write(f'\n x1: {x1}')
    data.write(f'\n x2: {x2}')