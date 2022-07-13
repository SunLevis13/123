# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# def find_sum(x):
#     s=0
#     for i in range(1,x+1):
#         s +=i
#     print(f'Сумма цифр числа {num} = {s}')
# num = int(input('Введите число: '))
# find_sum(num)

# num = int (input('Введите число: '))
# ran = range(1,num+1)
# numbers = list(ran)
# print (numbers)
# i = 0
# sum = 0
# while i < len(numbers):
#     sum += numbers[i]
#     i+=1
# print (f'sum = {sum}')

# num = int (input("Введите целое: "))
# sum = 0
# if num >= 1:
#     sum = sum + num % 10
#     num = num // 10
#     print(sum)

# print("Сумма цифр числа равна:", sum)


def func(num):
    str_num = str(num)
    str_num = str_num.replace('.', '')  # 31415926
    lst_str = list(str_num)  # ['3', '1', '4', '1', '5', '9', '2', '6']
    print(lst_str)
    sum=0
    
    for i in range(len(lst_str)):
        sum += int((lst_str[i]))
        
    print(f'Сумма цифа числа {num} = ',sum)
num = float(input('Введите вещественное число: '))
func(num)

