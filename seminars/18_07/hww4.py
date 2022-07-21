# Задана натуральная степень k.
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
import os
import random
import itertools

k = int(input('Задайте натуральную степень k: '))
def fillArrayRandom(size:int, N1:int, N2:int):
    size = k+1
    array = []
    for i in range(size):
        array.append(random.randrange(N1, N2))
    return array
rand_list = fillArrayRandom(k,0,101)
print(rand_list)

def get_func(k,rand_list):
    str1 = ['*x**']*(k-1) + ['*x']
    mnogochlen = [[a, b, c] for a, b, c  in itertools.zip_longest(rand_list, str1, range(k, 1, -1), fillvalue = '') if a !=0]
    print(mnogochlen)

    for x in mnogochlen:
        x.append(' + ') # проставляем + между кортежами
    mnogochlen = list(itertools.chain(*mnogochlen)) # объединяем в один список
    print(mnogochlen)
    mnogochlen[-1] = ' = 0' # добавляем концовочку (меняем последний '+' на '= 0')
    return "".join(map(str, mnogochlen)) # возвращаем строку

list = get_func(k, rand_list)
print(list)

path = os.path.join('folder','hw4.txt')
with open(path, 'w') as data:
    data.write(list)
