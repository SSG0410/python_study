s = input()
temp = 0

for i in s:
    print(i, end='')
    temp+=1
    if temp>9:
        print('')
        temp=0
