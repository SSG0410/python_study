list = [int(input()) for i in range(9)]

for i in range(9):
    for j in range(i+1, 9):
        if sum(list)-list[i]-list[j]==100:
            n1, n2 = list[i], list[j]
            list.remove(n1)
            list.remove(n2)
            break
    if len(list)<9:
        break

list.sort()
for i in list:
    print(i)