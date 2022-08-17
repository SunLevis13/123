import data_base


def create (): #получаем значения
    
    style = 'style="font-size:22px;"' # стиль шрифта в html представлении
    html = '<html>\n <head></head>\n <body>\n' # шаблон представления html
    html += '    <p {}>Name: {} </p>\n'\
        .format(style,data_base.name_data())
    html += '    <p {}>Tel.number: {} </p>\n'\
        .format(style,data_base.tel_data())
    html += '   </body>\n</html>'
  

    with open ('name_tel.html','a',encoding="utf-8") as page: # создаем файл html  и сохраняем его
        page.write(html)
    
    return html