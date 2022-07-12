# Реализуйте алгоритм перемешивания списка.
# spisok = [1, 2, 3, 4, 5]
# for item in spisok[::-1]: #проходит по индексам и перемещает элемент на индекс-1
#     print(item, end=' ')

# через while
# spisok = [1, 2, 3, 4, 5, 6]
# new_spisok = []

# i = 0
# while i < len(spisok):
#     item = spisok[len(spisok)-i-1]
#     new_spisok.append(item)

#     i += 1

# print(new_spisok)

# через for
spisok = [1, 2, 3, 4, 5, 6]
new_spisok = []

for i in range(len(spisok)):
    new_spisok.append(spisok[len(spisok) - i - 1])
print(new_spisok)