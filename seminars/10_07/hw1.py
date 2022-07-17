# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
def func(num):
    str_num = str(num)
    str_num = str_num.replace('.', '')  # 31415926
    lst_str = list(str_num)  # ['3', '1', '4', '1', '5', '9', '2', '6']
    print(lst_str)
    sum=0
    
    for i in range(len(lst_str)):
        sum += int(lst_str[i])
        
    print(f'Сумма цифа числа {num} = ',sum)
num = float(input('Введите вещественное число: '))
func(num)

