# -*- coding: utf-8 -*-
import datetime
import json
import csv
import io
import statistics
import pandas as pd


def write_json(data):
    """    
    Сохраняет данные в файл dataset.json
    """
    with open('ms_dataset.json', 'w', encoding="utf-8") as file:
        json.dump(data, file, indent=2, ensure_ascii=False)

def write_csv(data):
    """    
    Сохраняет данные в файл в dataset.csv
    """

    with io.open('ms_dataset.csv', 'a', encoding="utf-8", errors="ignore") as file:
        write = csv.writer(file)
        write.writerow(list(data.values()))

def write_stat_csv(data, filename):
    
    with io.open(filename, 'a', encoding="utf-8", errors="ignore") as file:
        write = csv.writer(file)
        write.writerow(data)

start = datetime.datetime.now()


data = json.load(open('cs_data_60_day_5363_items.json', encoding="utf-8"))

dataset =[]

variables = ('квартира',
            'хрущевка',
            'улучшенной',
            'брежневка',
            'старой',
            'проект',
            'свердловка',
            'сталинка',
            'нестандартная',
            'новостройка',
            'многокомнатная',
            'левый берег',
            'ленинский',
            'правобережный',
            'орджоникидзевский',
            'поселок',
            'агаповка',
            'другой р-н',
            'кол-во комнат',
            'общ площадь',
            'жил площадь',
            'кухня',
            'этаж',
            'ремонт',
            'соcтояние', 
            'окна',
            'балкон',
            'балкон застеклен',
            'торг',
            'ипотека',
            'срочно',
            'цена 1кв м'
            )

for item in data['14']:
    set_item = {i:0 for i in variables}
    if 'однок' in item[1].lower():
        set_item['кол-во комнат'] = 0.2
    elif 'двухк' in item[1].lower():
        set_item['кол-во комнат'] = 0.4
    elif 'трехк' in item[1].lower():
        set_item['кол-во комнат'] = 0.6
    elif 'четыр' in item[1].lower():
        set_item['кол-во комнат'] = 0.8
    elif 'пятик' in item[1].lower()\
    or 'многок' in item[1].lower():
        set_item['кол-во комнат'] = 1.0
    
    if 'однок' in item[1].lower()\
    or 'двухк' in item[1].lower()\
    or 'трехк' in item[1].lower()\
    or 'четыр' in item[1].lower()\
    or 'пятик' in item[1].lower()\
    or 'многок' in item[1].lower():
        set_item['квартира'] = 1
    else:
        if 'дом' in item[7].lower():
            set_item['дом'] = 1

    if 'хрущ' in item[1].lower():
        set_item['хрущевка'] = 1
    if 'улучш' in item[1].lower():
        set_item['улучшенной'] = 1
    if 'брежнев' in item[1].lower():
        set_item['брежневка'] = 1
    if 'стар' in item[1].lower():
        set_item['старой'] = 1
    if 'прое' in item[1].lower():
        set_item['проект'] = 1
    if 'сверд' in item[1].lower():
        set_item['свердловка'] = 1
    if 'нестан' in item[1].lower():
        set_item['нестандартная'] = 1
    if 'новост' in item[1].lower():
        set_item['новостройка'] = 1
    if 'сталин' in item[1].lower():
        set_item['сталинка'] = 1
    if 'многок' in item[1].lower():
        set_item['многокомнатная'] = 1

    if 'левый' in item[1].lower()\
    or 'левый' in item[2].lower()\
    or 'левый' in item[7].lower()\
    or 'левый' in item[8].lower():
        set_item['левый берег'] = 1

    elif 'ленинск' in item[2].lower():
        set_item['ленинский'] = 1
    elif 'правоб' in item[2].lower():
        set_item['правобережный'] = 1
    elif 'орджо' in item[2].lower():
        set_item['орджоникидзевский'] = 1    
    elif 'агапов' in item[2].lower() or 'агапов' in item[7].lower():
        set_item['агаповка'] = 1
    elif 'посёлок' in item[1].lower() or 'поселок' in item[1].lower()\
    or 'посёлок' in item[7].lower() or 'поселок' in item[7].lower()\
    or 'приурал' in item[1].lower() or 'светлый' in item[1].lower()\
    or 'западный' in item[1].lower() or 'счастливый' in item[1].lower()\
    or 'green' in item[1].lower() or 'раздолье' in item[1].lower()\
    or 'крылова' in item[1].lower() or 'радужный' in item[1].lower()\
    or 'нежный' in item[1].lower() or 'хуторки' in item[1].lower()\
    or 'соты' in item[1].lower() or 'александр' in item[1].lower()\
    or 'малиновы' in item[1].lower() or 'звездный' in item[1].lower()\
    or 'звёздный' in item[1].lower() or 'грин' in item[1].lower()\
    or 'прибреж' in item[1].lower():
        set_item['поселок'] = 1  
    else:
        set_item['другой р-н'] = 1

    if '/' in item[4]:
        if item[4].split('/')[0] == '1':
            set_item['этаж'] = 0.25
        elif item[4].split('/')[0] == item[4].split('/')[1]:
            set_item['этаж'] = 0.5
        elif item[4].split('/')[0] != item[4].split('/')[1]:
            set_item['этаж'] = 1

    if item[5]:
        set_item['общ площадь'] = item[5]
    if item[6] and len(item[7]) < 10:
        set_item['жил площадь'] = item[6]
    if item[7] and len(item[7]) < 6:
        set_item['кухня'] = item[7]

    if 'качеств' in item[7] and 'ремонт' in item[7]\
    or 'качеств' in item[8] and 'ремонт' in item[8]:
        set_item['ремонт'] = 1
    elif 'капит' in item[7] and 'ремонт' in item[7]\
    or 'капит' in item[8] and 'ремонт' in item[8]:
        set_item['ремонт'] = 1         
    elif 'не требует' in item[7] and 'ремонт' in item[7]\
    or 'не требует' in item[8] and 'ремонт' in item[8]:
        set_item['ремонт'] = 1
    elif 'хорош' in item[7] and 'ремонт' in item[7]\
    or 'не требует' in item[8] and 'ремонт' in item[8]:
        set_item['ремонт'] = 0.5
    elif 'требует' in item[7] and 'ремонт' in item[7]\
    or 'требует' in item[8] and 'ремонт' in item[8]:
        set_item['ремонт'] = 0
    elif 'соcтоян' in item[7] and 'обычн' in item[7]\
    or 'соcтоян' in item[8] and 'обычн' in item[8]:
        set_item['ремонт'] = 0.33
    elif 'соcтоян' in item[7] and 'хорош' in item[7]\
    or 'соcтоян' in item[8] and 'хорош' in item[8]:
        set_item['ремонт'] = 0.66
    elif 'соcтоян' in item[7] and 'отличн' in item[7]\
    or 'соcтоян' in item[8] and 'отличн' in item[8]:
        set_item['ремонт'] = 1

    if 'окна' in item[8] and 'пластик' in item[8]:
        set_item['окна'] = 1

    if 'балкон' in item[8] or 'лоджия' in item[8]:
        set_item['балкон'] = 1

    if 'торг' in item[7] or 'торг' in item[8]:
        set_item['торг'] = 1

    if 'ипотека' in item[7] or 'ипотека' in item[8]:
        set_item['ипотека'] = 1

    if 'срочно' in item[7] or 'срочно' in item[8]:
        set_item['срочно'] = 1

    if item[9] and item[5]:
        set_item['цена 1кв м'] =  str(int(item[9])/float(item[5]))

    if set_item['квартира']: # and 0.1*30 < float(set_item['цена 1кв м']) < 1.9*30: 
        dataset.append(set_item)


print('Всего записей: ', len(data['14']))
print('Подготовлено: ', len(dataset), ' строк данных для анализа')

csv_count = 0
for x in dataset:
    write_csv(x)
    csv_count += 1
print('csv file Done! ', csv_count, ' item save!')

write_json([list(i.values()) for i in dataset])
print('json file Done!')

print('Выбрано и сохранено: ', len(dataset), ' строк данных для анализа')

# блок статистики по умолчанию отключен

# array_stat = [float(i['цена 1кв м']) for i in dataset]
# mode_data = statistics.mode(array_stat)
# array_stat_f = [i for i in array_stat if mode_data*0.1 < i < mode_data*1.9]
# print('Данных после очистки от выбросов: ', len(array_stat_f),
# 'Осталось/отсеяно %: ', round(len(array_stat_f)/len(array_stat)*100, 2),' ## ',
# round(((len(array_stat) - len(array_stat_f))/len(array_stat))*100,2))
# print(' Цена кв м:\n',
#         ' средн арифм:', round(statistics.mean(array_stat), 3), ' <=> ',
#         round(statistics.mean(array_stat_f), 3),'\n',
#         ' медиана:', round(statistics.median(array_stat), 3), ' <=> ',
#         round(statistics.median(array_stat_f), 3),'\n',
#         ' мода:', round(statistics.mode(array_stat), 3), ' <=> ',
#         round(statistics.mode(array_stat_f), 3),'\n',
#         ' станд. отклонение:', round(statistics.pstdev(array_stat), 0), ' <=> ',
#         round(statistics.pstdev(array_stat_f), 0),'\n',
#         ' дисперсия:', round(statistics.pvariance(array_stat), 0),' <=> ',
#         round(statistics.pvariance(array_stat_f), 0)
#         )

# csv_countgr = 0
# for x in array_stat_pd: 
#     write_stat_csv(x, 'array_stat.csv')
#     csv_countgr += 1
# print('csv_gr file Done! ', csv_countgr, ' item save!')

# csv_countch = 0
# for x in array_stat_f:
#     write_stat_csv(x, 'array_stat_f.csv')
#     csv_countch += 1
# print('csv_ch file Done! ', csv_countch, ' item save!')

stop = datetime.datetime.now()
print('Время выполнения: ', stop-start)