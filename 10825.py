import sys
input = sys.stdin.readline

n = int(input())
list = [input().split() for i in range(n)]
list.sort(key=lambda x : (-int(x[1]), int(x[2]), -int(x[3]), x[0]))
for i in list:
    print(i[0])
