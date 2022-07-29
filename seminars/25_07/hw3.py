# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
def find_sum(x):
    res2 = 1
    # for i in range(1,x+1):
    i=0
    res = [i for i in range(1,x+1)]
    print(res)
    for i in range(len(res)):
        res2 *= res[i]
        i+=1
    
    print(f'Произведение от 1 до {N} = ', res2)

N = int(input('Введите число: '))
find_sum(N)