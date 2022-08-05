from pickle import FALSE, TRUE


n = int(input())

stack=[]
ans=[]
count=1
temp=TRUE

for i in range(n):
    num = int(input())

    while count<=num:
        stack.append(count)
        ans.append('+')
        count+=1
    
    if stack[-1]==num:
        stack.pop()
        ans.append('-')
    
    else:
        temp=FALSE

if temp==FALSE:
    print('NO')

else:
    for i in ans:
        print(i)