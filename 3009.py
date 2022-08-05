list1=[]
list2=[]
for i in range(3):
    a, b = input().split()
    list1.append(a)
    list2.append(b)

for i in list1:
    if list1.count(i)==1:
        print(i, end=' ')

for i in list2:
    if list2.count(i)==1:
        print(i, end=' ')