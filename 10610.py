s = list(map(int, input()))
temp = 0

if (0 not in s) or (sum(s)%3!=0):
    print('-1')
else:
    s.sort()
    s.reverse()
    for i in s:
        print(int(i), end='')
