a = int(input())
b = int(input())

sum=0
list=[]

for i in range(a, b+1):

    for j in range(2,i+1):
        if i%j==0:
            if i==j:
                list.append(i)
                sum+=i
            break
if sum==0:
    print(-1)
else:
    print(sum)
    print(min(list))