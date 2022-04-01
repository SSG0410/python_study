n = int(input())
list = list(map(int, input().split()))

list.sort()
ans = 0
for i in list:
    ans+=i*n
    n-=1

print(ans)