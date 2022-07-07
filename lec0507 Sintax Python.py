# синтаксис

# value = None
# a = 123
# b = 1.23
# print (type(a))
# print (type(b))
# value = 1234
# print (type(value))

# s = 'hello world'
# print(s) # вывод строки
# s = "hello 'world"
# print(s) # вывод строки
# s = 'hello \'world'
# print(s)
# s = 'hello \nworld'
# print(s)
# a = 123
# b = 1.23
# s = 'hello \'world'
# print(a,b,s)
# print(a,'-',b,'-',s)
# print('{} - {} - {}'.format(a,b,s))
# print(f'{a} - {b} - {s}')
# print('{1} - {2} - {0}'.format(a,b,s))

# f = True
# print(f)
# f = False
# print(f)

# s = 'СПИСКИ (массив)'
# list = []
# print(list)
# list = [1,2,3]
# print(list)
# list = ['1','2','3','hello world']
# print(list)

# list = ['1','2','3','hello world',1,2,4.5,True]
# print(list)

# print('Введите a')
# a = input()
# print('Введите b')
# b = input()
# print(a, b)
# print('{} {}'.format(a, b))
# print(f'{a} {b}')
# print(a, '+', b, '=', a+b)

# print('Введите a')
# a = int(input())
# print('Введите b')
# b = int(input())
# print(a, b)
# print('{} {}'.format(a, b))
# print(f'{a} {b}')
# print(a, '+', b, '=', a+b)

# print('Введите a')
# a = float(input())
# print('Введите b')
# b = float(input())
# print(a, b)
# print('{} {}'.format(a, b))
# print(f'{a} {b}')
# print(a, '+', b, '=', a+b)

# Арифметические операции
# +, -,*, /, %, //,**
# Приоритет операций
# **, ⊕, ⊖,*, /, //, %, +, -
# ( ) Скобки меняют приоритет

# a = 123
# b = 321
# c = a+b
# print(c) # сумма

# a = 123
# b = -321
# c = a+b
# print(c) # унарный минус

# a = 2
# b = 8
# c = a-b
# print(c)

# a = 2
# b = 8
# c = a * b
# print(c)

# a = 2
# b = 8
# c = a / b
# print(c)

# a = 12
# b = 8
# c = a // b
# print(c)

# a = 12
# b = 8
# c = a % b
# print(c)

# a = 2
# b = 4
# c = a ** b
# print(c)

# a = 1.3
# b = 3
# c = a * b
# print(c)

# a = 1.3
# b = 3
# c = round(a * b)
# print(c)

# a = 1.3
# b = 3
# c = round(a * b,3)
# print(c)

# a=3
# a+=5 # аналог a=a+5
# print(a)

# Логические операции
# >, >=, <, <=, ==, !=
# not, and, or – не путать с &, |,^
# Кое-что ещё: is, is not, in, not in

# a=1<4
# print(a)

# a = 1>4
# print(a)

# a = 1<4 and 5>2
# print(a)

# a = 1 == 2
# print(a)

# a = 1 != 2
# print(a)

# a = 'qwe'
# b = 'qwe'
# print(a==b) # сравнение строк

# a = [1,2]
# b = [1,2]
# print (a==b) # сравнение происходит по элементам списков

# func =1
# T = 4
# x = 2
# print(func<T>x)

# f = 1>2 or 4<6
# print(f)

# f =[1,2,3,4]
# print(f)
# print(not 2 in f)

# f =[1,2,3,4]
# # check = f[0] % 2 == 0
# check = not f[0] % 2
# print(f)
# print(check)

#  Управляющие конструкции
#  if, if - else

# a = int(input('a = '))
# b = int(input('b = '))
# if a > b:
#     print(a)
# else:
#     print(b)


# username = input('Введите имя: ')
# if username == 'Маша':
#  print('Ура, это же МАША!')
# elif username == 'Марина':
#  print('Я так ждала Вас, Марина!')
# elif username == 'Ильнар':
#  print('Ильнар - топ)')
# else:
#  print('Привет, ', username)

#  Управляющая конструкция WHILE

# original = 23
# inverted = 0
# while original != 0:
#  inverted = inverted * 10 + (original % 10)
#  original //= 10
# print(inverted)

#  Управляющая конструкция WHILE-ELSE:

# original = 23
# inverted = 0
# while original != 0:
#     inverted = inverted * 10 + (original % 10)
#     original //= 10
# else:
#     print('Пожалуй')
#     print('хватит :)')
# print(inverted)

#  Управляющая конструкция FOR:

# for i in 1,2,3,4,5:
#     print(i**2)

# list = [1,2,3,10,5]
# for i in list:
#     print(i)

# r = range(5)
# for i in r:
#     print(i)

# for i in range(5): # аналог выше в одну строку
#     print(i)

# for i in range(1,10,2): # Диапазон и приращение 2
#     print(i)

# for i in 'qwerty':
#     print(i)

# text = 'приходи в гости'
# print(text[0]) # п
# print(text[1]) # р
# print(text[len(text)-1]) # и
# print(text[-5]) # г
# print(text[:]) # print(text)
# print(text[:2]) # пр
# print(text[len(text)-2:]) # ти
# print(text[2:5]) # ихо
# print(text[1:-5]) # риходи в
# print(text[0:len(text):3]) # пхи с
# print(text[::3]) # пхи с
# print(text[2:9] + text[-5] + text[:2]) # иходи вгпр

# numbers = list(range(1,5))
# numbers[0]=10
# # print(numbers)
# for i in numbers:
#     i *= 2
#     print(i)
# print(numbers)

# colors = ['red', 'green', 'blue']
# for e in colors:
#  print(e) # red green blue
# for e in colors:
#  print(e*2) # redred greengreen blueblue
# colors.append('gray') # добавить в конец
# print(colors == ['red', 'green', 'blue', 'gray']) # True
# colors.remove('red') #del colors[0] # удалить элемент
# print(colors)

# ФУНКЦИИ
def f(x):
    if x == 1:
     return 'Целое'
    elif x == 2.3:
     return 23
    else:
     return

arg = 2.3
print(f(arg))
print(type(f(arg))) # int

print(f(1)) # Целое
print(f(2.3)) # 23
print(f(28)) # None
print(type(f(1))) # str
print(type(f(2.3))) # int
print(type(f(28))) # NoneType
