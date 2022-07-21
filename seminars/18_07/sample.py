# path = 'file.txt'
# with open(path,'r') as f:
#     data = f.read()
#     print(data)

# path = 'file.txt'
# with open(path,'w') as f:
#     f.write('asd\n')
#     f.write('asd')
#     f.write('asd')
#     print(f)

path = 'file.txt'
with open(path,'a') as f:
    f.write('\nwork\n')
    print(f)

