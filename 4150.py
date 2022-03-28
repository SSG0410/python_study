n = int(input())
f=[0,1,1]
for i in range(2,n):
    f.append(f[i]+f[i-1])

print(f[n])