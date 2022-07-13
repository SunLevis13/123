# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.

# def spisok (x):
#     posled=0
#     for i in range (1,x):
#         posled = posled + pow((1+1/spisok[i]),spisok[i])
#         print(posled)

# spisok(n)
        
    # for i in posled:
    #     posled.append( posled[pow((1+1/spisok[i]),spisok[i])] )
#     #     i+=1
#     return posled
# print(spisok)


# n1 = int(input('Введите число n1 '))
# n2 = int(input('Введите число n2 '))
# n3 = int(input('Введите число n3 '))
# n4 = int(input('Введите число n4 '))
# n5 = int(input('Введите число n5 '))

# func [] = int [1,2,3,4,5]
# new_f = []

# for i in range(len(func)):
#     new_f.append(func[pow((1+1/func[len(func)-i-1]),func[len(func)-i-1])])
# print(new_f)

def func(x):
    new_f = []
    f = range(1,x) # 1 2 3 4
    spisok = list(f) # [1, 2, 3, 4]
    print(spisok) 
    sum = 0
    for i in range(len(f)):
        new_f.append (round((pow((1+1/spisok[len(spisok)-i-1]),spisok[len(spisok)-i-1])),3))
        sum += new_f[i]
    print(new_f)
    print(f'Сумма элементов = ',sum)
func(int(input('Введите число: ')))


