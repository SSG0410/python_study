n = int(input())

a = list(map(int, input().split()))
sum = []
sum.append(a[0])

for i in range(n-1):
    if a[i+1]>=a[i+1]+sum[i]:
        sum.append(a[i+1])
    else:
        sum.append(a[i+1]+sum[i])

print(max(sum))