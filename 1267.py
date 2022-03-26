n=int(input())
list=map(int, input().split())
sum_Y=0
sum_M=0

for i in list:
    sum_Y+=(i//30+1)*10
    sum_M+=(i//60+1)*15

if sum_Y==sum_M:
    print('Y M %d'%sum_Y)
elif sum_Y<sum_M:
    print('Y %d'%sum_Y)
else:
    print('M %d'%sum_M)
