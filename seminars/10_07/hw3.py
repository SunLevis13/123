# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.
def spisok (x):
    posled=0
    for i in range (1,x):
        posled = posled + pow((1+1/spisok[i]),spisok[i])
        print(posled)
n = int(input('Введите число n1 '))
spisok(n)
        
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
