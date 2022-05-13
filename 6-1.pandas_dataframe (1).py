import pandas as pd
from collections import OrderedDict

# data=pd.Series(['Hong',100])
#data=pd.Series(['Hong',100],index=['name','score'])  #index를 문자로 지정

#dictionary 이용 방법
data = pd.DataFrame({
    'Name': ['Hong', 'Choi', 'Lee', 'Kang'],
    'Age': [37, 25, 41, 55],
    'Born': ['1965-26-25', '1982-03-04', '1991-07-28', '2000-11-19']}
    , index=['teacher', 'student', 'staff', 'teacher']  # index 지정
    , columns=['Name', 'Born', 'Age']  # columns 순서가 바뀜
)

#data=pd.DataFrame(OrderedDict([('Name':['Rosaline', 'William']), ('Occupation':['Chemist', 'Statistician'])]) #작동 안함

# 시리즈 선택
first_row = data.loc['student']
print(first_row)
print(type(first_row))


#data = pd.DataFrame([['Hong',37,'1965-26-25'],['Choi', 41,'1982-03-04'],['Lee',25,'2000-11-19'],['Kang',55, '1991-07-28']])
#data = pd.DataFrame([['Hong',37,'1965-26-25'],['Choi', 41,'1982-03-04'],['Lee',25,'2000-11-19'],['Kang',55, '1991-07-28']], index=['teacher', 'student', 'staff', 'teacher'], columns=['Name', 'Born', 'Age']) # columns 순서가 바뀜)  # index 지정
#    , columns=['Name', 'Born', 'Age']  # columns 순서가 바뀜

print(data)
