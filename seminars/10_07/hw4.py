# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях.

def find_proiz(N):
    ran = range(-N, N+1)
    print(ran)
    numbers = list(ran)
    print(numbers)

    s = 1
    for i in range(-N, N+1):
        s *= i
        print(s)
    print(f'Произведение чисел от {-num} до {num} = {s}')
    
num = int(input('Введите число: '))
find_proiz(num)
