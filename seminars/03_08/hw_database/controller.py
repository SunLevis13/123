# import datatime
import files
# from logger import name_logger
# from logger import tel_logger

def start_table():
    with open ('name_tel.csv','a') as page:
        page.write('|             NAME             |             TEL             |\n')
        page.write('______________________________________________________________\n')

def name_receive():
    a = input('Введите ФИО: ')
       
    with open ('name_tel.csv','a', encoding="utf-8") as page: # создаем файл csv  и сохраняем его
            page.write(f'  {a}')
    files.name_logger(a)
    return a

    
def tel_receive():
    b = str(input('Введите телефон: '))
    
    if b.isdigit() == True:
        with open ('name_tel.csv','a') as page: # создаем файл csv  и сохраняем его
            
            page.write(f'                {b}\n')
            page.write('______________________________________________________________\n')
    else:
        b = input('Введите телефон, используя только цифры:')
        if b.isdigit() == True:
            with open ('name_tel.csv','a') as page: # создаем файл csv  и сохраняем его
                
                page.write(f'                {b}\n')
                page.write('______________________________________________________________\n')
    files.tel_logger(b)
    return b
    

    # data_base(name,tel)
    # view_data(text='|')


