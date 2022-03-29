a, b = input().split()
min = int(a)+int(b)
max = int(a)+int(b)

for i in range(len(a)):
    if a[i]=='5':
        max += 10**(len(a)-i-1)
    if a[i]=='6':
        min -= 10**(len(a)-i-1)

for i in range(len(b)):
    if b[i]=='5':
        max += 10**(len(b)-i-1)
    if b[i]=='6':
        min -= 10**(len(b)-i-1)


print(min, max)