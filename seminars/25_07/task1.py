# Задайте последовательность чисел. Напишите программу, которая выведет список
# неповторяющихся элементов исходной последовательности.
lst = [1,1,2,3,1,45,6,27,2,13,9]
# res = list(filter(lambda x: lst.count(x) == 1, lst))
# print(res)

# через включение - List Comprehention
res = [x for x in lst if lst.count(x) < 2]
print(res)

# распаковка кортежа через *
def f(x1,x2):
    return x1*x2

a=(1,2)
print(f(*a))
