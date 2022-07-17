# 11. найти факториал числа
n = int (input('Введите число n = '))
i = 1
factorial = 1
while i<=n:
    factorial*=i
    i+=1
print(f'Factorial {n} = {factorial}')