a = int(input())

for i in range(a):
    sum=0
    data = list(input())

    for j in data:
        if j=='(':
            sum+=1
        else:
            sum-=1
        if sum<0:
            print('NO')
            break
    if sum > 0:
        print('NO')
    elif sum==0:
        print('YES')
