# Сформировать список из  N членов последовательности.
# Для N = 5: 1, -3, 9, -27, 81 и т.д.

# def searchNumber(a,b):
#     my_list = [1]
#     i=1
#     while len(my_list) < a:
#         my_list.append(my_list[i-1]*b)
#         i+=1
#     print (my_list)

# searchNumber(5,-3)

# 2 способ
# def func(x):
#     s = 1
#     print(s, end=' ')
#     for i in range(1, x):
#         s = s * -3
#         print(s, end=' ')

# n = int(input('Введите число n = '))
# func(n)

def searchNumber(a:int,b:int) ->list:
    my_list = [1]
    while len(my_list) < a:
        my_list.append(my_list[-1]*b)
    return my_list

print(searchNumber(5,-3))