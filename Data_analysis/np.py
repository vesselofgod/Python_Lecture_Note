import numpy as np
import matplotlib.pyplot as plt

#X축 데이터 생성
x=np.linspace(0,2*np.pi,100)
#y축 생성
y=np.sin(x)
#그래프 그리기
plt.plot(x,y)
plt.show()




'''
list1=[1,2,3,4]
a=np.array(list1)
# array의 형태(크기)를 확인할 수 있다.

#이 경우에는 list의 크기가 4이므로 (4,)가 출력됨
print(a.shape)
#데이터의 타입을 확인할 수 있다.
print(a.dtype)

b = np.array([[1,2,3],[4,5,6]])
#이 경우에는 데이터는 2*3 행렬이므로 (2,3)이 출력된다.
print(b.shape)
print(b[0,0])

#0부터 2까지 4등분해서 나눈 숫자를 저장함.
c=np.linspace(0,2,4)
print(c)

d=a-c
#각각의 원소들에 뺄샘 연산을 수행함.
print(d)
'''
