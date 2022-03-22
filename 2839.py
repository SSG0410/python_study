a = int(input())
cnt=0

while a>=0:
    if a%5==0:
        cnt=cnt+(a//5)
        print(cnt)
        break
    
    a=a-3
    cnt=cnt+1

else:
    print(-1) 