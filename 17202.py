a=list(input())
b=list(input())
total=[]
temp=[]
for i in range(8):
    total.append(a[i])
    total.append(b[i])

while len(total)>2:
    for i in range(1,len(total)):
        temp.append((int(total[i-1])+int(total[i]))%10)
    total=temp
    temp=[]

for i in total:
    print(i, end='')
    