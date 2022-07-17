# a = []

# def func(my_list: list)-> None:
#     my_list.append(1)

# func(a)
# func(a)
# func(a)

# print(a)

def func(my_list = []):
    my_list.append(1)
    print(my_list)

func()
func()
func()