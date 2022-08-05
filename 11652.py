import sys
input = sys.stdin.readline

n = int(input())
list = list(int(input()) for i in range(n))
dict = {}

for i in list:
    if i not in dict:
        dict[i]=1
    else:
        dict[i]+=1

dict = sorted(dict.items(), key=lambda x: (-x[1],x[0]))
print(dict[0][0])