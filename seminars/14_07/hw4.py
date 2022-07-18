# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

def func(num):
    new_lst=[]
    while num !=0:
        k = num%2
        num = num//2
        new_lst.append(k)
        print(num)

    print(new_lst)
    
func(int(input('Введите число: ')))
