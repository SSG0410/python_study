import sys
input=sys.stdin.readline
n=int(input())
s=[input().split() for i in range(n)]
s.sort(key=lambda x: int(x[0]))
for i in range(n):
    print(s[i][0], s[i][1])