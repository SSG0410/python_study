n=int(input())
list=[1,2,3]

for i in range(n):
    a, b = map(int, input().split())
    x = list.index(a)
    y = list.index(b)
    list[x], list[y] = list[y], list[x]

print(list[0])