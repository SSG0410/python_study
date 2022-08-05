s=[]
temp=[]
for i in range(8):
    s.append(int(input()))
    temp.append(s[i])
sum=0
index=[]
temp.sort()

for i in range(3,8):
    sum+=temp[i]
    index.append(s.index(temp[i])+1)

print(sum)
index.sort()
for i in index:
    print(i, end=' ')
