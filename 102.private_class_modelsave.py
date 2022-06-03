import numpy as np

import tensorflow as tf
import keras as k
import pandas as pd
#공부시간 X와 성적 Y의 리스트를 만듭니다.
'''
x = np.array([[2, 0], [4, 4], [6, 2], [8, 3]])
y = np.array([[81], [93], [91], [97]])
'''
data = [[2, 0, 81], [4, 4, 93], [6, 2, 91], [8, 3, 97]]
x = [[i[0],i[1]] for i in data]
y = [i[2] for i in data]
print(x,y)
'''
data = pd.read_csv('score.csv')
dataset=data.values
x=dataset[:,0:2]
y=dataset[:,2]
print(x)
print(y)
...
'''
np.random.seed(3)
model = k.models.Sequential()
model.add(k.layers.Dense(2, input_dim=2))
model.add(k.layers.Dense(4))
model.add(k.layers.Dense(1))

model.compile(loss='mean_squared_error', optimizer='adam')

# 훈련
model.fit(x, y, epochs=510,verbose=1) # 100번 반복 훈련

model.save('model.h5')

model = k.models.load_model('model.h5')

# 테스트
a=int(input("stutime?"))
b=int(input("private?"))
print(model.predict([[a,b]]))  # 입력이 5일 때 결과값 출력

