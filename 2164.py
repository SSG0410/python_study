n = int(input())
list = [i for i in range(n,0,-1)]

while len(list)>1:
    list.pop()
    temp=list[len(list)-1]
    del list[len(list)-1]
    list.insert(0,temp)

for i in list:
    print(i)