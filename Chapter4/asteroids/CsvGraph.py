import csv
import matplotlib.pyplot as plt

f= open('CsvPracticeExam.csv')
data=csv.reader(f)

x=[]
male=[]
female=[]
label=[]
n=0
for row in data:
    if row[0] != '행정구역':
        print(row)
    else:
        x.append(row[0])
