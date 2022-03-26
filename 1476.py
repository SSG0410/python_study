e, s, m = map(int, input().split())
e2, s2, m2 = 0,0,0
num = 0

while True:
    e2+=1
    s2+=1
    m2+=1
    num+=1
    if e2==16:
        e2=1
    if s2==29:
        s2=1
    if m2==20:
        m2=1
    if (e==e2 and s==s2 and m==m2):
        break

print(num)