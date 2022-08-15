from datetime import datetime as dt
from time import time
from pathlib import Path

def name_logger(x):
    time=dt.now()#.strftime('%H:%M') # получили данные о времени в формате час:минута
    with open('logtelname.csv','a') as log_file: # создали файл log.csv куда записываем данные
        log_file.write('----------------------------------------')
        log_file.write('\n Time of adding new data: {}\n' .format(time))
        # log_file.write('\nName: {} {} Num2: {} \nResult: {}\n' .format(x,y))
        log_file.write('Name: {}\n' .format(x))

def tel_logger(x):
    time=dt.now()#.strftime('%H:%M') # получили данные о времени в формате час:минута
    with open('logtelname.csv','a') as log_file: # создали файл log.csv куда записываем данные
        log_file.write('----------------------------------------')
        log_file.write('\n Time of adding new data: {}\n' .format(time))
        log_file.write('Tel: {}\n' .format(x))