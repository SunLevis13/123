# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.
import os
import itertools
path1 = os.path.join('folder','hw5_1.txt')

with open(path1,'r') as data:
    nums1 = list(map(str,data.read().split(' ')))
print(nums1)

path2 = os.path.join('folder','hw5_2.txt')

with open(path2,'r') as data:
    nums2 = list(map(str,data.read().split(' ')))
print(nums2)

a = [int(nums1[0][:-5]), int((nums1[1]+ nums1[2])[:-2]), int((nums1[3]+ nums1[4]))]
print(a)

b = [int(nums2[0][:-5]), int((nums2[1]+ nums2[2])[:-2]), int((nums2[3]+ nums2[4]))]
print(b)



[k1,k2,k3] = [(a[0]+b[0]),a[1]+b[1],a[2]+b[2]]
data = [k1,k2,k3]
new_list=list(map(str, data))
print(new_list)

def get_func(data,new_list):
    str1 = ['*x**']*(len(data)-1) + ['*x']
    mnogochlen = [[a, b, c] for a, b, c  in itertools.zip_longest(new_list, str1, range(len(data)-1,1,-1), fillvalue='') if a !=0]
    print(mnogochlen)

    for x in mnogochlen:
            x.append(' + ') 
    mnogochlen = list(itertools.chain(*mnogochlen)) 
    print(mnogochlen)
    mnogochlen[-1] = ' = 0' 
    return "".join(map(str, mnogochlen)) 

list = get_func(data, new_list)
print(list)

path = os.path.join('folder','hw5_done.txt')
with open(path, 'w') as data:
    data.write(list)
