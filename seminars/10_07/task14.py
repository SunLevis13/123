# Пользователь задаёт две строки. Определить количество вхождений одной строки в другой.
# st1 = 'привет Мир, привет'
# st2 = 'привет'
# t = 0
# for i in range(len(st1)):
#     if(st1[i:i + len(st2)] == st2):
#         t += 1
#     print(i)
# print(f'---> t = {t}')

# через функцию
# st1 = 'приветт Мирт'
# st2 = 'т'

# def str(st1,st2):
#     t = 0
#     for i in range(len(st1)):
#         if(st1[i:i + len(st2)] == st2):
#             t += 1
#     return t
# print(str(st1,st2))

# через while
# st1 = 'приветт Мирт'
# st2 = 'т'
# i=0
# count=0
# while(True):
#     i=st1.find(st2,i)
#     if i == -1:
#         break
#     else:
#         i += 1
#         count+=1
# print(count)

# способ через count

def find_sym(string1:str, strin2:str):
    print(string1.count(strin2))

first_string = input('Введите текст:')
second_string = input('Введите текст:')
find_sym(first_string,second_string)
