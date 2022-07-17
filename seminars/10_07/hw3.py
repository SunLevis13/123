# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.

def func(x):
    new_f = []
    f = range(1,x+1) # 1 2 3 4
    spisok = list(f) # [1, 2, 3, 4]
    print(spisok) 
    sum = 0
    for i in range(len(f)):
        new_f.append (round((pow((1+1/spisok[len(spisok)-i-1]),spisok[len(spisok)-i-1])),3))
        sum += new_f[i]
    print(new_f)
    print(f'Сумма элементов = ',sum)
func(int(input('Введите число: ')))


