s = input()
prior = {'*':2, '/':2, '+':1, '-':1, '(':0}
stack = []
ans = ''

for i in s:
    if i.isalpha():
        ans+=i
    
    else:
        if i=='(':
            stack.append(i)
        elif i==')':
            while True:
                temp  = stack.pop()
                if temp=='(':
                    break
                ans+=temp
        else:
            while stack and prior[stack[-1]]>=prior[i]:
                ans+=stack.pop()
            stack.append(i)

while stack:
    ans+=stack.pop()

print(ans)