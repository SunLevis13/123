#  1 метод
# path = r'folder\task1.txt'
# with open (path, 'r') as f:
#     text = f.readline()

# def convert_to_int(str):
#     return[int(x) for x in str.split( )]
# int_list = convert_to_int(text)

# print(int_list)
# print(max(int_list))
# print(min(int_list))

# 2 метод
# path = r'folder\task1.txt'
# with open (path, 'r') as f:
#     text = f.readlines()
# print(text)

# text_split = text[0].split(' ')
# print(text_split)

# min = int(text_split[0])
# max = int(text_split[0])

# for i in text_split:
#     if int(i) < min:
#         min = int(i)
#     if int(i) > max:
#         max = int(i)

# print(min)
# print(max)

#  3 метод
def is_int(str:str) -> bool:
    try:
        int(str)
        return True
    except ValueError:
        return False

def input_list_in_numbers(str_in:str) -> list:
    list_dirty = str_in.split(' ')
    list_clean=[]
    for elem in list_dirty:
        if is_int(elem):
            list_clean.append(int(elem))
    return list_clean

path = r'folder\task1.txt'
with open (path, 'r') as f:
    str_in = f.readline()
print(str_in)

numb_list = input_list_in_numbers(str_in)

print(numb_list)
print(max(numb_list))
print(min(numb_list))