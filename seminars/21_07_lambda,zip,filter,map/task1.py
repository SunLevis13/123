# В файле находятся N натуральных чисел, записанных через пробел. Срнди чисел не хватает одного, чтобы выполнялось условие
# A[i] -1 = A[i-1]. Найдите это число.

path = r'folder21_07/task1.txt'
with open (path, 'r') as f:
    str_in = f.readline()
print(str_in)