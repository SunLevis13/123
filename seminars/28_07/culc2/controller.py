import oper
from view import input_data, view_data

def btm():
    num_data = (int(input('Первое число: ')), int(input('Второе число: ')))
    znak = input_data('Укажите действие: ')
    match znak:
        case '+':
            res = oper.summ(*num_data)
        case '-':
            res = oper.dif(*num_data)
    view_data(text='Результат: ', data=res)

