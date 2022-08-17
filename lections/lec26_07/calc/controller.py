import model_mult as model # если нужна сумма, то соот-но ссылаемся на model_sum и т.п. На тот файл, где нужная сейчас операция
import view

def button_click():
    value_a = view.get_value() #получаем данные из view
    value_b = view.get_value()
    model.init(value_a, value_b)
    result = model.do_it() #делает нужную операцию с переменными из файла model
    view.view_data(result, "result") # передаем result в файл view