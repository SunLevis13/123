# colors = ['red','green','blue']
# data = open('file.txt','w')
# data.writelines(colors)
# data.write('\nLine123\n')
# data,close()

# with open('file.txt','w') as data:
#     data.write('Line 1\n')
#     data.write('Line 2\n')

# path = 'file.txt'
# data = open(path,'r')
# for line in data:
#     print(line)
# data.close()

# import lec0507SintaxPython
# print(lec0507SintaxPython.f(1))

# import lec0507SintaxPython as lec
# print(lec.f(1))

# def func(*params):
#     res: int = 0
#     for item in params:
#         res += item
#     return res
# print(func(1,2,3,4))

# (a,b) = (3,4)
# print(a)

# a = (3,4)
# print(a)
# print(a[0])

# a = (3,4,5)
# for item in a:
#     print(item)


# dictionary = {}
# dictionary = \
#     {
#         'up': '↑',
#          'left': '←',
#          'down': '↓',
#          'right': '→'
#     }
# print(dictionary)  # {'up':'↑', 'left':'←', 'down':'↓', 'right':'→'}
# print(dictionary['left']) 

# for k in dictionary.keys():
#     print(k)

# for k in dictionary.values():
#     print(k)


from re import A


a = {1,2,3,4}
b = {2,3,4,5}
i = a.intersection(b)
print(i)

q = a\
    .union(b)\
    .difference(a.intersection(b))
print(q)
