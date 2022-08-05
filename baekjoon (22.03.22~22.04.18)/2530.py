a, b, c = map(int, input().split())
d = int(input())

a = (d//3600)+a
b = (d%3600)//60+b
c = (d%60)+c

if c>=60:
    b = c//60+b
    c = c%60

if b>=60:
    a = b//60+a
    b = b%60

if a>=24:
    a =a%24
    
print(a, b, c)