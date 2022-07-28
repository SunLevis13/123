import html_creater as hc
import xml_generator as xg


print(hc.create())
print(xg.create())

import data_provider as dp # для метода вывода температуры в фаренгейтах

hc.new_create(xg.new_create(dp.data_collection()))
