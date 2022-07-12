# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
def find_sum(x):
    proizv = 1
    for i in range(1,x+1):
        proizv *=i
        
    print('Произведение от 1 до N = ', proizv)

N = int(input('Введите число: '))
find_sum(N)