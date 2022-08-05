s = list(input())
count0 = 0
count1 = 0
for i in range(1, len(s)):
    if s[i-1]!=s[i] and s[i]=='1':
        count1+=1
    elif s[i-1]!=s[i] and s[i]=='0':
        count0+=1

print(max(count0, count1))