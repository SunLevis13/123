# Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

lst = list(map(float, input("Введите числа через пробел: ").split()))
new_lst = [round(i%1,3) for i in lst if i%1 != 0]
print(new_lst)
str_lst = str((max(new_lst) - min(new_lst))*10).replace('.','')
print(str_lst)