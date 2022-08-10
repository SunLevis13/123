# import datatime
# from view import view_data
# from data import data_base
# from data import a,b


def start_table():
    with open ('name_tel.csv','a') as page:
        page.write('|             NAME             |             TEL             |\n')
        page.write('______________________________________________________________\n')

def btm():
    a = input('Введите ФИО: ')
    b = str(input('Введите телефон: '))
    # with open ('name_tel.csv','a', encoding="utf-8") as page:
        
    #     page.write('______________________________________________________________\n')
    if b.isdigit() == True:
        with open ('name_tel.csv','a', encoding="utf-8") as page: # создаем файл csv  и сохраняем его
            page.write(f'  {a}')
            page.write(f'                {b}\n')
            page.write('______________________________________________________________\n')
    else:
        b = input('Введите телефон, используя только цифры:')
        if b.isdigit() == True:
            with open ('name_tel.csv','a', encoding="utf-8") as page: # создаем файл csv  и сохраняем его
                page.write(f'  {a}')
                page.write(f'                {b}\n')
                page.write('______________________________________________________________\n')
    return a,b
    
    # data_base(name,tel)
    # view_data(text='|')


    # data_logger(a,b)