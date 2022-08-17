from user_interface import temperature_view
from user_interface import wind_speed_view
from user_interface import pressure_view

def create (device = 1): #с какого-то девайса получаем значения
    style = 'style="font-size:22px;"' # стиль шрифта в html представлении
    html = '<html>\n <head></head>\n <body>\n' # шаблон представления html
    html += '    <p {}>Temperature: {} c</p>\n'\
        .format(style,temperature_view(device))
    html += '    <p {}>Wind_speed: {} m/s</p>\n'\
        .format(style,wind_speed_view(device))
    html += '    <p {}>Pressure: {} mmHg</p>\n'\
        .format(style,pressure_view(device))
    html += '   </body>\n</html>'

    with open ('index.html','w') as page: # создаем файд html  и сохраняем его
        page.write(html)
    
    return html

def new_create (data): #с какого-то девайса получаем значения
    t, p, w = data
    t = t * 1.8 + 32 # перевод температуры в фаренгейт
    style = 'style="font-size:22px;"' # стиль шрифта в html представлении
    html = '<html>\n <head></head>\n <body>\n' # шаблон представления html
    html += '    <p {}>Temperature: {} f</p>\n'\
        .format(style,t)
    html += '    <p {}>Wind_speed: {} m/s</p>\n'\
        .format(style,w)
    html += '    <p {}>Pressure: {} mmHg</p>\n'\
        .format(style,p)
    html += '   </body>\n</html>'

    with open ('new_index.html','w') as page: # создаем файл html  и сохраняем его
        page.write(html)
    
    return data