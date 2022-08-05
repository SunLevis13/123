from datetime import datetime as dt
from time import time
from pathlib import Path

def data_logger(x,y,z,l):
    time=dt.now()#.strftime('%H:%M') # получили данные о времени в формате час:минута
    with open('logculc.csv','a') as log_file: # создали файл log.csv куда записываем данные
        log_file.write('----------------------------------------')
        log_file.write('\n Time of adding new data: {}\n' .format(time))
        log_file.write('\nNum1: {} {} Num2: {} \nResult: {}\n' .format(x,l,y,z))
