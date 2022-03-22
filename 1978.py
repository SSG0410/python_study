a = int(input())
b = map(int, input().split())
b = list(b)
count=0

for i in b:
    for j in range(2, i+1):
        if i%j == 0:
            if i==j:
                count+=1
            break

print(count)

