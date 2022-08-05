n=int(input())
word=input()
b=[]
stack=[]

for i in range(n):
    b.append(int(input()))

for i in word:
    if i.isalpha():
        stack.append(b[ord(i)-65])
    else:
        str2=stack.pop()
        str1=stack.pop()
        if i=='+':
            ans=str1+str2
            stack.append(ans)
        elif i=='-':
            ans=str1-str2
            stack.append(ans)
        elif i=='*':
            ans=str1*str2
            stack.append(ans)
        elif i=='/':
            ans=str1/str2
            stack.append(ans)

print('%.2f'%stack[0])