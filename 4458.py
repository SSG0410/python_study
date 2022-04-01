import sys
input = sys.stdin.readline

n = int(input())

for i in range(n):
    s = list(input())
    if ord(s[0])<97:
        for j in s:
            print(j, end='')
    else:
        s[0]=chr(ord(s[0])-32)
        for j in s:
            print(j, end='')