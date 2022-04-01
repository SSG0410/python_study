import sys
input = sys.stdin.readline

n = int(input())
for i in range(n):
    sum = 0
    s = list(input())
    s.pop()
    s = set(s)
    for j in s:
        sum +=ord(j)
    print(2015-sum)