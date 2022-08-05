class Book():
    def __init__(self): # init - конструктор класса, он собирает поля (название, год, автор и т.п.)
        self.age = 2022
        self.auth = 'Discord = love'
        self.name = 'Python = love'

    def open_book(self, mes: str = 'Hello'): # метод - открыть книгу и сказать Hello
        print(mes)



my_book_1 = Book()
my_book_1.open_book(mes = "Hello, friend!")
# my_book_1.age = 1990
print(my_book_1.age)
print(my_book_1.name)
print()

# Чтобы каждый раз не указывать отдельную переменную my_book_1.age = 2005, my_book_1.auth = 'Bunin' и т.д., переменные можно сразу запрашивать
class Book():
    def __init__(self, age, auth, name): # можно также def __init__(self, age: int=0, auth: str='None', name: str='None') - задали значения по умолчанию
        self.age = age
        self.auth = auth
        self.name = name

    def open_book(self, mes: str = 'Hello'): # метод - открыть книгу и сказать Hello
        print(mes)



my_book_1 = Book(age = 2005, auth = 'Bunin',name = 'OOP')
print(my_book_1.age)
print(my_book_1.name)
print(my_book_1.auth)
