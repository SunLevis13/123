# word = 'абв Ура, питон круто, очень интересно! абвг'
# ask_col = input("Введите искоючающие символы одной строкой: ")
# word = word.split()
# print(word)

# result = [i for i in word if ask_col not in i]
# print (result)

# 2 способ(не читает рус текст?)
# def read_text(f_name:str)->str:
#     with open (f_name,'r') as f:
#         return f.readline()

# a = read_text('task3.txt').split()
# b = ' '.join(filter(lambda x: 'абв' not in x,a))
# print(b)

# 3 способ через filter
word = 'абв Ура, питон круто, очень интересно! абвг'
def del_words(word):
    word = list(filter(lambda x: 'абв' not in x,word.split()))
    return ' '.join(word)

word = del_words(word)
print(word)
