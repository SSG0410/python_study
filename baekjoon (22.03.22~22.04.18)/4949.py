import sys
input = sys.stdin.readline

while True:
    stack = []
    flag = 0
    line = input().rstrip()

    if line == '.':
        break

    for i in line:
        if i=='(' or i=='[':
            stack.append(i)
        elif i==')':
            if not stack or stack[-1]=='[':
                flag = 1
                break
            else:
                stack.pop()
        elif i==']':
            if not stack or stack[-1]=='(':
                flag = 1
                break
            else:
                stack.pop()
    
    if flag==0 and not stack:
        print('yes')
    else:
        print('no')