import view
import data

def button_click():
    value_a = view.in_count()
    value_b = view.in_count()
    data.init(value_a, value_b)
    result = data.sum
    view.view_data(result)
    