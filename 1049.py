n, m = map(int, input().split())
list = [1000,1000]

for i in range(m):
    a, b = map(int, input().split())
    list[0]=min(list[0],a)
    list[1]=min(list[1],b)

cnt = n//6+1
ans = 100000000000
for i in range(cnt+1):
    result=0
    temp=n
    temp-=i*6
    result+=i*list[0]
    if temp>0:
        result+=temp*list[1]
    ans=min(ans, result)

print(ans)