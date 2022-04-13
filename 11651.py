import sys
input = sys.stdin.readline
n = int(input())
list = [list(map(int,input().split())) for i in range(n)]
list.sort(key=lambda x: (x[1],x[0]))

for i in range(n):
    print(list[i][0], list[i][1])
