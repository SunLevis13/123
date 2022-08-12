from controller import name_receive
from controller import tel_receive

def create (a,b): #получаем значения
    style = 'style="font-size:22px;"' # стиль шрифта в html представлении
    html = '<html>\n <head></head>\n <body>\n' # шаблон представления html
    html += '    <p {}>Name: {} </p>\n'\
        .format(style,name_receive(a))
    html += '    <p {}>Tel.number: {} </p>\n'\
        .format(style,tel_receive(b))
    html += '   </body>\n</html>'
  

    with open ('name_tel.html','a') as page: # создаем файл html  и сохраняем его
        page.write(html)
    
    return html