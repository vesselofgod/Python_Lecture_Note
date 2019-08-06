import csv
import matplotlib.pyplot as plt

f = open('CsvPracticeExam.csv', 'rt', encoding='UTF8')
data = csv.reader(f)

male=[]
female=[]
labels=[]
n=0
for row in data:
    if row[0] != '\ufeff행정구역':
        male.append(row[1])
        female.append(row[2])
        labels.append(row[0])
        n+=1
x=[i for i in range(n)]
plt.title("age graph")
plt.grid(True)
plt.xlim(1,n)
plt.xticks(x,labels,rotation="vertical")
plt.plot(x,male,'r:',label='male')
plt.plot(x,female , 'b--', label='female')
plt.legend(loc=2)
plt.show()
