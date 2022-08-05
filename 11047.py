n, k = map(int, input().split())
list = [int(input()) for i in range(n)]
list.reverse()
ans = 0
for i in list:
    ans+=k//i
    k=k%i
print(ans)