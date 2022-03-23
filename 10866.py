#덱
import sys

n = int(input())
deque = []

for i in range(n):
    com = sys.stdin.readline().split()

    if com[0]=='push_front':
        deque.insert(0,com[1])        
    elif com[0]=='push_back':
        deque.append(com[1])
    elif com[0]=='pop_front':
        if len(deque)==0:
            print('-1')
        else:
            print(deque.pop(0))
    elif com[0]=='pop_back':
        if len(deque)==0:
            print('-1')
        else:
            print(deque.pop())
    elif com[0]=='size':
        print(len(deque))
    elif com[0]=='empty':
        if len(deque)==0:
            print('1')
        else:
            print('0')
    elif com[0]=='front':
        if len(deque)==0:
            print('-1')
        else:
            print(deque[0])
    elif com[0]=='back':
        if len(deque)==0:
            print('-1')
        else:
            print(deque[len(deque)-1])
