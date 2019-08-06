import csv
f=open('a.csv')
data = csv.reader(f)
List=[]
c=0
for row in data:
    if row[2]=='자전거':
        List.append(row[1])
        c+=1
print(List)
