n = int(input())

s = [0,1,3]
sum = 4

for i in range(3, n+1):
    if i%2==0:
        s.append(sum+2)
        sum+=s[i]
    else:
        s.append(sum+1)
        sum+=s[i]

print(s[n]%10007)