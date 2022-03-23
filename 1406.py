import sys

stack_l = list(input())
stack_r = []

n = int(input())

for i in range(n):
    com = sys.stdin.readline().split()

    if com[0]=='L' and stack_l:
        stack_r.append(stack_l.pop())
    elif com[0]=='D' and stack_r:
        stack_l.append(stack_r.pop())
    elif com[0]=='B' and stack_l:
        stack_l.pop()
    elif com[0]=='P':
        stack_l.append(com[1])

stack_r.reverse()

print("".join(stack_l+stack_r))