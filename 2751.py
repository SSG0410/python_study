import sys

n = int(input())
list = [int(sys.stdin.readline()) for i in range(n)]

list.sort()

for i in list:
    print(i)