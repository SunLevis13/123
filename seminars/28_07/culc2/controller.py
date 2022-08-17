import oper
import data
from view import input_data, view_data
from logger import data_logger
from data import a,b

def btm():
    num_data = (int(input('Первое число: ')), int(input('Второе число: ')))
    data.init_data(*num_data)
    znak = input_data('Укажите действие: ')
    match znak:
        case '+':
            res = oper.summ(*data.return_data())
        case '-':
            res = oper.dif(*data.return_data())
        case _:
            res = 'NONE'
    view_data(text='Результат: ', data=res)


    data_logger(a,b,res,znak)

