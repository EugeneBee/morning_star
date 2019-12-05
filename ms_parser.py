# -*- coding: utf-8 -*-
import urllib.request
import datetime
import re
import json
from bs4 import BeautifulSoup

def write_json(data):
    """    
    Сохраняет данные в файл cs_data.json
    """
    with open('ms_data.json', 'w', encoding="utf-8") as file:
        json.dump(data, file, indent=2, ensure_ascii=False)

start = datetime.datetime.now()

#задаем грубину получения данных в днях
len_day = 60
result_dict = {'14':[], '17':[]}
data = []
count_items = 0
#цикл постраничной загрузки данных
for date_url in range(1,len_day+1):

#адрес страницы для загрузки данных (url)
    url = 'http://www.citystar.ru/detal.htm?cid=2&dt=' + str(date_url)

    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'lxml')

    rows = soup.find_all('tr', attrs={'class':'tbb'})
    for row in rows:
         cols = row.find_all('td', attrs={'class':'ttx'})
         cols = [ele.text.strip() for ele in cols]
         data.append([ele for ele in cols]) # Get rid of empty values
            
# строки данных о продаже имеют длину 14 или 17 отбор по условию
for item in data:
    if item:
        if len(item) == 14 or len(item) == 17:
            result_dict[str(len(item))].append(item)
            count_items += 1

#сообщение в консоль о количестве записей и времени выполнения
print('Найдено и сохранено: ', count_items, 'записей объявлений')
stop = datetime.datetime.now()
print(stop-start)
