#이분탐색
import sys
input = sys.stdin.readline

n = int(input())
a = input().split()
a.sort()
m = int(input())
b = input().split()

for i in b:
    left, right = 0, n-1
    flag = 0

    while True:
        med = (left+right)//2
        if i == a[med]:
            print(1)
            flag = 1
            break
        elif i > a[med]:
            left = med+1
        elif i < a[med]:
            right = med-1
        
        if left>right:
            break

    if flag==0:
        print(0)


# 집합자료형
'''
for i in b:
    if i in a:
        print(1)
    else:
        print(0)
'''