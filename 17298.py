n = int(input())
list = list(map(int, input().split(' ')))
ans=[]

for i in range(n):
    if list[i] == max(list):
        print('-1', end=' ')
    else:
        for j in range(i+1,n):
            if list[i]>=list[j]:
                continue
            else:
                print(list[j], end=' ')
                break