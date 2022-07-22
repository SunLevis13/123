import os

numbers = "1 2 3 5 6 7 8 9"
path = os.path.join('folder21_07','task1.txt')

with open(path,'r') as data:
    f = data.readline()
print(f)

list_int = list(map(int,[i for i in f.split()]))
print(list_int)

result = list(filter(lambda i: list_int[i] - list_int[i-1] != 1,range(1,len(list_int))))
print(result[0]+1)

# способ через функцию
def f(list_int:list):
    for i in range (1,len(list_int)):
        if list_int[i] - list_int[i-1] != 1:
            return list_int[i-1]+1
    return "Not found"
print (f(list_int))