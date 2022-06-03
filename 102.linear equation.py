import numpy as np
import keras as k

# 훈련용 데이터
x_train = [ 1,  2,  3,  4,  5,  6,  7,  8,  9, 10]  # 입력
y_train = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]  # 결과

np.random.seed(3)
# 모델 생성
model = k.models.Sequential()
# 입력 값은 1차원 자료: input_dim=1
model.add(k.layers.Dense(1, input_dim=1))
#model.add(k.layers.Dense(4))
#model.add(k.layers.Dense(1))

# 최적화 방식

# cost/loss 함수로 컴파일 작업
#adam=k.optimizers.Adam(lr=0.001,beta_1=0.9, beta_2=0.999, epsilon=1e-08, decay=0.0)
model.compile(loss='mean_squared_error', optimizer='adam')

# 훈련
model.fit(x_train, y_train, epochs=2000,verbose=1)  # 100번 반복 훈련 verbose : 훈련정보

# 테스트
print(model.predict(np.array([30])))  # 입력이 5일 때 결과값 출력