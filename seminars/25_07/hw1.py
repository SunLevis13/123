# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
def func(num):
    str_num = str(num)
    # str_num = str_num.replace('.', '')  # 31415926
    lst_int = list(map(int,[i for i in str_num.replace('.', '')]))
    # lst_str = list(str_num)  # ['3', '1', '4', '1', '5', '9', '2', '6']
    print(lst_int)
    
    sum=0
    for i in range(len(lst_int)):
        sum += int(lst_int[i])
        
    print(f'Сумма цифа числа {num} = ',sum)
num = float(input('Введите вещественное число: '))
func(num)

