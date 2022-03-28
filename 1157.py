word = (input().upper())
list = list(set(word))
cnt = []

for i in list:
    cnt.append(word.count(i))

if cnt.count(max(cnt))>1:
    print("?")

else:
    print(list[cnt.index(max(cnt))])
