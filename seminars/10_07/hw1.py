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

num = 3.1415926
str_num = str(num)
str_num = str_num.replace('.', '')  # 31415926
lst_str = list(str_num)  # ['3', '1', '4', '1', '5', '9', '2', '6']
print(lst_str)
print(type(lst_str))
i = 0
sum = 0
print(len(lst_str))  # 8
for i in range(len(lst_str)):
    n = int(input(lst_str[i]))
    sum += n
    i += 1
    
print(sum)
# print(n)
# sum += lst_str[i]
# i+=1
# print(i)


# lst_num = map(int, lst_str)
# s = sum(lst_num)
# print(s)
