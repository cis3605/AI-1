import pandas as pd
import numpy as np

#arr1 = np.array([1,2,3,4,5])
#s = pd.Series([1, 3, 5, 7, 9])  # Series 데이터 생성, index 디폴트 생성
#print(arr1)
#print(s)
#s1=s.drop(3) #3번 index 삭제
#print(s1)

#arr=np.array([0,2,4,8,10])  #numpy 배열로  Series 데이터 생성
#s=pd.Series(arr)

#s=pd.DataFrame([[1,2,3],[4,5,6]])  #DataFrame 데이터 생성
#s = pd.DataFrame([[1, 2, 3], [4, 5, 6]], columns=['a', 'b', 'c'])

# index
#s = pd.Series([1, 3, 5, 7, 9], index=['a','b','c','d','e'])  # Series 데이터 생성
#s1=s.drop('c')
#print(s1)

s = pd.DataFrame(np.random.randn(10, 7), columns=['a', 'b', 'c', 'd', 'e', 'f', 'g'])
#s = pd.DataFrame(np.random.randn(5, 7),index=['a','b','c','d','e'], columns=['a', 'b', 'c', 'd', 'e', 'f', 'g'])
print(s)

#s = pd.DataFrame(np.random.randn(10, 7))
#print(s[(5<s.index) & (s.index<10)]) # 5보타 크고 10보다 작은 인덱스에 해당되는 행을 출력
#s = pd.DataFrame(np.random.randn(5, 7),index=['a','b','c','d','e'], columns=['a', 'b', 'c', 'd', 'e', 'f', 'g'])
#print(s)
#print(s.values) #pandas에 있는 numpy data
#print(s[('b'<s.index) & (s.index<'d')])

# print(s.head()) # 인덱스번소 상위 5개 출력
# print(s.head(7)) # 인덱스번호 상위 7개 출력
# print(s.tail())  # 인덱스번소 하위 5개 출력
#print(s.columns)  # columns 출력
# print(s.index)    # Index 출력
#print(s.describe()) #컬럼별로 통계 출력, std : 표준편차
#print(s['a'].describe())
# print(s['c'])  #'c' 컬럼 데이터만 출력
#print(s[['c','d']])  #'c','d' 컬럼 데이터만 출력
#print(s[2:5])  #index값 2 부터 4번까지 출력

#print(s.iloc[1])  # index가 1인 행들의 데이터 (location)
# 1. 행번호(row number)로 선택하는 방법 (.iloc)
# 2. label이나 조건표현으로 선택하는 방법 (.loc)

# .iloc : 행이든 열이든 숫자로 location을 나타내서 Selecting or indexing 하는 방법입니다."
'''
data = pd.DataFrame(np.random.randn(5, 7),index=['a','b','c','d','e'], columns=['a', 'b', 'c', 'd', 'e', 'f', 'g'])
print(data)
print(data.iloc[0]) # data의 첫번째 행만
print(data.iloc[1]) # 두번째 행만
print(data.iloc[-1]) # 마지막 행만
# Columns:
print(data.iloc[:,0]) # 첫번째 열만
print(data.iloc[:,1]) # 두번째 열만
print(data.iloc[:,-1]) # 마지막 열만

print(data.iloc[0:5]) # 첫 5개행만
print(data.iloc[:, 0:2]) # 첫 2개열만
print(data.iloc[[0,3], [0,5,6]]) # 1st, 4th, 7th, 25th 행과 + 1st 6th 7th 열만
print(data.iloc[0:5, 5:8]) # 첫 5개 행과 5th, 6th, 7th 열만

print(data.loc['a']) # Andrade 행만 선택
print(data.loc[['a','b']])
'''
#print(s[-1 < s])  # -1보다 큰 값만 출력, 조건에 맞지 않으면 NaN 출력
#d = s[-1 < s]
#print(d.dropna())   # NoN이 있는 행은 제거
#print(d.fillna(10))  # NoN을 10으로 치환
#print (s.mean()) # 행 방향 평균
#print (s.mean(1)) # 열 방향 평균
#s['c']=1  #'c'열 모두 1로 치환
#s['c']=[1,2,3,4,5,6,7,8,9,10]  #'c'열 해당 값으로 치환
#s['d'][3]=1  ##'d'열 3행만  1로 치환
#s['d'][3:7]=1  ##'d'열 3부터 6행까지 1로 치환
#print(s)
d1 = pd.DataFrame(np.random.randn(10, 7), columns=['a', 'c', 'd','g','k','l','m'])
#d2=pd.concat([s,d1]) #s프레임과 d프레임을 이어 붙임 컬럼 수는 일치해야한다. 컬럼 이름은 달라도 된다.
#print(d2)

d2=pd.concat([s,s,s])  #인덱스가 중복 됨
d2=d2.reset_index(drop=True) #index를 reset, drop=True : 기존 index를 버림
#print(d2)
#print(d2.drop(5))  #5번 index에 해당되는 값드을 삭제(세건)
print(s.drop('f',axis=1))  #d열 삭제, axis=1 : 세로임을 나타 냄, 0은 가로값
print(s.drop(3,axis=0))  #3행 삭제, axis=0 : 세로임을 나타 냄, 0은 가로값
print(s)