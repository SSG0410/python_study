s=list(input())
alpha=[-1]*26
num=0

for i in s:
    if alpha[ord(i)-97]==-1:
        alpha[ord(i)-97]=num
        num+=1
    else:
        num+=1
for i in alpha:
    print(i, end=' ')