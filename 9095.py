t = int(input())

for i in range(t):
    s=[0,1,2,4]
    n = int(input())
    for j in range(4,n+1):
        s.append(s[j-3]+s[j-2]+s[j-1])
    print(s[n])
