import numpy as np
from numpy.core._multiarray_umath import ndarray

#arr = np.zeros(10)
#arr = np.zeros((3, 5)) #3행 5열 0으로 채움
#arr = np.zeros((2, 3, 5)) #2면 3행 5열
#arr = np.ones(5) #1로 5개 채움
#arr = np.arange(10)  #0부터 9까지
#arr = np.arange(5,10) #5부터 9가지
#arr = np.random.rand(5,3) #0과 1사이의 난수 matrix array 생성

#arr = np.random.randn(5,3) #가우시안 표준 정구 분포에서  난수 matrix array 생성 (평균 0, 표준편치 1)
# 평균과의 차이를 편차, 편차의 합은 0, 분산 : 편차 제곱을 평균  표준편차 : 분산의 제곱근
#arr = np.random.randint(1,20) #1부터 19사이의 난수 1개
#np.random.shuffle(arr) # 기존 데이터 순서 바꾸기, data는 2개 이상이어야 함
#print(arr)
#arr1 = np.random.choice(arr)  #1차원만 가능
#arr1 = np.random.choice(arr, size=5)  # 기존 데이터에서 sampling
#arr1 = np.random.choice(arr, size=5,replace=True) #True이면 한번 선택한 데이터를 다시 선택 가능
#arr1 = np.random.choice(arr, size=10,replace=True, p=[0.1, 0, 0.3, 0.6, 0])  # 선택 확률을 다르게 해서 5개 선택
#print (arr)
#print (arr1)
'''
np.random.choice(a, size=None, replace=True, p=None)

a : 배열이면 원래의 데이터, 정수이면 arange(a) 명령으로 데이터 생성
size : 정수. 샘플 숫자
replace : 불리언. True이면 한번 선택한 데이터를 다시 선택 가능
p : 배열. 각 데이터가 선택될 수 있는 확률
'''
#arr = np.unique   # 중복데이터 제거
'''
numpy.unique(arr, return_index, return_inverse, return_counts)
arr
입력 배열, 1차원 배열이 아니면 병합됩니다.
return_index : 값이 True면 입력 배열의 요소들의 인덱스들을 리턴합니다.
return_inverse : 값이 True면 입력 배열을 재구성할 떄 쓰이는 고유 배열의 인덱스들을 반환합니다.
return_counts : 값이 True면 중복 되지 않는 요소들이 입력 배열에 나타난 회 수를 리턴합니다.
'''

a = np.array([5, 2, 6, 2, 7, 5, 6, 8, 2, 9])

print ('기본 배열:')
print (a)

'''
print ('중복데이터 제거:')
print (np.unique(a))

print ('배열요소의 인덱스:')
u, index = np.unique(a, return_index=True) #값이 True면 입력 배열의 요소들의 인덱스들을 리턴합니다.
print (index)
print(u)

'''
'''
print ('고유 배열의 인덱스:')
u, index = np.unique(a, return_inverse=True) #값이 True면 원 배열의 원소가 재 배열의 해당 인덱스.
print(index)
print (u)

print ('고유 배열의 인덱스:')
print (index)

print ('인덱스를 사용하여 원래 배열 재구성:')
print (u[index])

print ('고유 요소의 반복 횟수 반환:')
u, index = np.unique(a, return_counts=True) #값이 True면 중복 되지 않는 요소들이 입력 배열에 나타난 회 수를 리턴합니다.
print (u)
print (index)
'''


