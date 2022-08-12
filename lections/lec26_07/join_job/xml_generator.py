from user_interface import temperature_view
from user_interface import wind_speed_view
from user_interface import pressure_view

def create (device = 1): #с какого-то девайса получаем значения
    
    xml = '<xml>\n' # шаблон представления xml
    xml += '    <temperature_view units = "c">{}</temperature>\n'\
        .format(temperature_view(device))
    xml += '    <wind_speed_view units = "m/s">{}</wind_speed_view>\n'\
        .format(wind_speed_view(device))
    xml += '    <pressure_view units = "mmHg">{}</pressure>\n'\
        .format(pressure_view(device))
    xml += '   </xml>'

    with open ('data.xml','w') as page: # создаем файл xml  и сохраняем его
        page.write(xml)
    
    return xml

def new_create (data): #с какого-то девайса получаем значения
    t, p, w = data
    t = t * 1.8 + 32 # перевод температуры в фаренгейт
    xml = '<xml>\n' # шаблон представления xml
    xml += '    <temperature units = "f">{}</temperature>\n'\
        .format(t)
    xml += '    <wind_speed_view units = "m/s">{}</wind_speed_view>\n'\
        .format(w)
    xml += '    <pressure units = "mmHg">{}</pressure>\n'\
        .format(p)
    xml += '   </xml>'

    with open ('new_data.xml','w') as page: # создаем новый файл xml для фаренгейт  и сохраняем его
        page.write(xml)
    
    return data