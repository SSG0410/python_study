import sys

a = int(input())
#리스트이용
'''
for i in range(a):
    str = list(sys.stdin.readline().split())

    for j in str:
        print(j[::-1], end=' ')
'''

#stack이용
for i in range(a):
    str = input()
    str += " "
    stack = []

    for j in str:
        if j!=" ":
            stack.append(j)
        else:
            while stack:
                print(stack.pop(), end='')
            print(' ', end='')