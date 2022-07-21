# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

import os
path = os.path.join('folder','hw3.txt')

with open(path,'r') as data:
    numbers = list(map(int,data.read().split(' ')))
print(numbers)

def get_nums(x):
    list_num = []
    for e in x:
        if e not in list_num:
            list_num.append(e)
    return list_num

print(get_nums(numbers))


