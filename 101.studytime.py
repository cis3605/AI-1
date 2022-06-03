import numpy as np
import pandas as pd
import keras as k
import matplotlib.pyplot as plt

#공부시간 X와 성적 Y의 리스트를 만듭니다.
p=[0]
data = [[2, 81], [4, 93], [6, 91], [8, 97]]

x = [i[0] for i in data]
y = [i[1] for i in data]
x_data = np.array(x)
y_data = np.array(y)

'''
data1=(np.array(data))
x_data=data1[:,0]
y_data=data1[:,1]
print(x_data)
print(y_data)
#리스트로 되어 있는 x와 y값을 넘파이 배열로 바꾸어 줍니다.(인덱스를 주어 하나씩 불러와 계산이 가능해 지도록 하기 위함입니다.)
'''

np.random.seed(3)
model = k.models.Sequential()
#model.add(k.layers.Dense(1, input_dim=1))
model.add(k.layers.Dense(10, input_dim=1, activation='relu'))
#model.add(k.layers.Dense(10, input_dim=1))
model.add(k.layers.Dense(1))

#model.compile(loss='mean_squared_error', optimizer='SGD') #SGD 확률적 경사하강법
model.compile(loss='mean_squared_error', optimizer='Adam')
#metrics=['accuracy']  선형회귀모델에서는 사용 불가
# 훈련
model.fit(x_data, y_data, epochs=2000)  # 100번 반복 훈련


# 테스트
print(model.predict([6,4]))  # 입력이 5일 때 결과값 출력

#k=[1,2,3,4,5,6,7,8]
#print(model.predict(k))
