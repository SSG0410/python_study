num=1
while True:
    ans=0
    l, p, v = map(int, input().split(' '))

    if l==0 and p==0 and v==0:
        break
    
    ans=l*(v//p)
    ans+=min((v%p),l)
    print('Case %d: %d'%(num,ans))
    num+=1
