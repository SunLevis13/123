# Задайте список. 
# Напишите программу,кот. определит, присутствует ли в заданном списке строк некое число.

list_str = ['12543','2fghj371', 'dsk2567814']
f_num = input('Enter the number: ')
is_Found = False
for item in list_str:
    print(item)
    if item.__contains__(f_num):
        is_Found = True
        break
print(is_Found)

