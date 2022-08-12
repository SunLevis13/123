# import datatime

def start_table():
    with open ('name_tel.csv','a') as page:
        page.write('|             NAME             |             TEL             |\n')
        page.write('______________________________________________________________\n')

def name_receive():
    a = input('Введите ФИО: ')
       
    with open ('name_tel.csv','a', encoding="utf-8") as page: # создаем файл csv  и сохраняем его
            page.write(f'  {a}')
    
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
    return b



    # data_base(name,tel)
    # view_data(text='|')


    # data_logger(a,b)