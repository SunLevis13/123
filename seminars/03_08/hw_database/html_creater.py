from data import name_data
from data import tel_data

def create (): #получаем значения
    a = name_data()
    b = tel_data()
    style = 'style="font-size:22px;"' # стиль шрифта в html представлении
    html = '<html>\n <head></head>\n <body>\n' # шаблон представления html
    html += '    <p {}>Name: {} </p>\n'\
        .format(style,a)
    html += '    <p {}>Tel.number: {} </p>\n'\
        .format(style,b)
    html += '   </body>\n</html>'
  

    with open ('name_tel.html','a') as page: # создаем файл html  и сохраняем его
        page.write(html)
    
    return html