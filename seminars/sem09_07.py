# 1. По двум заданным числам проверить является ли одно квадратом второго 
# a = int (input('Введите число a = '))
# b = int (input('Введите число b = '))
# if b**2 == a:
#     print (f"Число {a} является квадратом числа {b}")
# elif a**2 == b:
#     print (f"Число {b} является квадратом числа {a}")
# else:
#     print ("Числа не являются квадратом друг друга")

# 2. Найти максимальное из пяти чисел
#       1способ
# numbers = list (range(-5,0))
# print (numbers)
# max = numbers[0]
# for i in numbers:
#       if i > max:
#         max = i
# print (f"Максимальное число {max}")

#      2 способ
# for i in range (1,6):
#     a = int(input(f'Введите число {i} = '))
#     if i == 1:
#         max = a
#     elif max < a:
#         max = a
# print (f"Максимальное число {max}")

# 3. Вывести на экран числа от -N до N
N = int (input('Введите число N = '))
print (list (range(-N,N+1)))