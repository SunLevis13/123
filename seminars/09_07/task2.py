
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
for i in range (1,6):
    a = int(input(f'Введите число {i} = '))
    if i == 1:
        max = a
    elif max < a:
        max = a
print (f"Максимальное число {max}")
