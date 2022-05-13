import pandas as pd
#import numpy as np

#data = pd.read_csv('test-1.csv')
#print(data)
#data.columns = ["a", "b", "c",'d','e','f'] #컬럼 이름 바꿈, 갯수가 맞아야 함
#data.index = ["10", "11", "12",'15','16'] #index 이름 바꿈, 갯수가 맞아야 함
#print(data)

#print(data.head()) #데이터프레임에서 가장 앞쪽에 있는 5개의 행을 출력
#print(data.head(10))  #데이터프레임에서 가장 앞쪽에 있는 10개의 행을 출력
#print(type(data)) #pandas 타입
#print (data.shape) # 테이터프레임의 행과 열의 크기
##### loc : index 기준   iloc : 행번호 기준
#print('-------------')
#print (data.loc[data.shape[0]-1]) #마지막 행을 출력 shap정보의 첫 열 값은 전체 행의 갯수이므로 마지막 행 번호는 '-1'을 해주면 된다.
#print (data.iloc[-1]) #마지막 행  출력
#print (data.iloc[[1,4]])  #해당 인덱스의 행만 출력
#print (data.loc[['11','15']])  #해당 인덱스의 행만 출력
#print (data.iloc[:,[2,4,-1]])  # 해당 열 출력 (B,D,마지막(F))
# print (data.iloc[:,range(0,6,2)]) #(0,2,4 열 출력)
# print (data.iloc[:,0:6:2]) #(0,2,4 열 출력)
# print (data.iloc[[1,5,8],[0,2,5]]) # 1,5,8행의 0,2,5번째 열 출력
#print (data.loc[[1,5,8],['A',"B",'C']])  # 1,5,8행의 A,B,C 열 출력
# print (data.loc[5:8,['A',"B",'C']])  # 5,6,7,8행의 A,B,C 열 출력
#print (data.columns)  #컬럼에 대한 정보
# print (data.dtypes) #구성하는 값의 자료형
#print (data.info()) #데이터셋에 대한 정보  28은 Non-null인 갯수

# print(data[['A', 'B']]) # #명시된 열 이름에 해당되는 열만 출력

# 행번호와 인덱스의 차이점 정확한 이해 필요

#print('==============================')
#pd.set_option('display.max_row', 5)
#data1 = pd.read_csv('test.csv')
#print(data1.loc[:,['A','B','C','D']])

#data2 = pd.read_csv('gapminder.tsv', sep='\t')  # csv는 기본적으로 ','로 구분되어져있다. 그러나 탭으로 구분되어진 파일은  sep='\t'을 명시해준다.
#data2 = pd.read_csv('sonar.csv')
#pd.set_option('display.max_row', None)  # 판다스 행을 무제한 확장  500은 작동 안함
#pd.set_option('display.max_row', 1704)  #1704열 출력  열의 갯수와 맞아야 합
#pd.set_option('display.max_columns', None)  # 판다스 열을 무제한 확장
#pd.set_option('display.width', 1000)
#pd.set_option('display.max_columns', 4)
#print(data2)
#print(data2.head(200))  #200 line만 출력


#print (data2.iloc[range(450,500)])  #500line 출력

#i=range(100,120) #첨자는 변수 가능
#print (data2.iloc[i])  #100 부터 120 열 출력

#print (data2.iloc[range(0,500)])

#print(data2)

#print(data2.groupby('year')['lifeExp'].mean())

#data3=data2.drop([2])  #2번째 행 삭제
#print(data3)

#data = pd.read_json('https://poloniex.com/public?command=returnTicker')
#print(data)
data = pd.read_csv('test.csv')
data.to_csv('test1.csv', index=False)  #csv 파일로 저장
