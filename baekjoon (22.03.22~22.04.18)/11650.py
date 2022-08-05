import sys
input = sys.stdin.readline
n = int(input())
list = [list(map(int,input().split())) for i in range(n)]
list.sort()

for i in range(n):
    print(list[i][0], list[i][1])
