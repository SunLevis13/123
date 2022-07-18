# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

list = [2,3,4,5,6,7,8]
list2 = []
for i in range(len(list)):
    if len(list)%2 == 0 and i < len(list)/2:
        list2.append(list[i] * (list[len(list)-i-1]))
    elif len(list)%2 != 0 and i < len(list)/2:
        list2.append(list[i] * (list[len(list)-i-1]))
print(list2)
