list = [int(input()) for i in range(5)]
for i in range(5):
    if list[i]<40:
        list[i]=40

print('%d'%(sum(list)/len(list)))