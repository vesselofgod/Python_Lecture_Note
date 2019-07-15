SelfNum=[]
for j in range(1,10001):
    SelfNum.append(j)
def sum_digit(number):
	result = 0
	for i in str(number):
		result += int(i)
	return result

for k in range(1,10001):
    n=sum_digit(k)+k
    if n<=10000 and n in SelfNum:
        SelfNum.remove(n)
for l in range(len(SelfNum)):
    print(SelfNum[l])
