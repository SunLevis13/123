from controller import btm
import controller

def create (device=1): #получаем значения
    style = 'style="font-size:22px;"' # стиль шрифта в html представлении
    html = '<html>\n <head></head>\n <body>\n' # шаблон представления html
    html += '    <p>Name: {} </p>\n'\
        .format(style,btm(device))
    html += '    <p>Tel.number: {} </p>\n'\
        .format(style,btm(device))
  

    with open ('name_tel.html','a') as page: # создаем файл html  и сохраняем его
        page.write(html)
    
    return html