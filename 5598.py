s = input()
ans = []
for i in s:
    if i=='A' or i=='B' or i=='C':
        ans.append(chr(ord(i)+23))
    else:
        ans.append(chr(ord(i)-3))

for i in ans:
    print(i, end='')