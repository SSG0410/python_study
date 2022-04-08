n = int(input())
list = list(int(input()) for i in range(n))
list.sort()
for i in list:
    print(i)
