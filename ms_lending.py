# -*- coding: utf-8 -*-
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import Normalizer
from keras.models import Sequential
from keras.layers.core import Dense
import numpy
import pandas

names = ('квартира',
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

array = pandas.read_csv('cs_datasets_60_day_3795.csv', names=names)
dataset = array.values
X = dataset[:,0:31]
Y = dataset[:,31]
scaler = Normalizer().fit(X)
normalizedX = scaler.transform(X)
numpy.set_printoptions(precision=3)
(trainX, testX, trainY, testY) = train_test_split(normalizedX, Y,
test_size=0.25, random_state=42)

model = Sequential()
model.add(Dense(128, activation='relu', input_shape=(trainX.shape[1],)))
model.add(Dense(1))
model.compile(optimizer='adam', loss='mse', metrics=['mae'])
model.fit(trainX, trainY, epochs=100, batch_size=1, verbose=2)
mse, mae = model.evaluate(testX, testY, verbose=0)

print("Средняя абсолютная ошибка (тысяч рублей): ", round(mae, 0))

pred = model.predict(testX)
print("Стоимость по рассчету модели: ", round(pred[1][0], 0))
print("Фактическая стоимость: ", testY[1])