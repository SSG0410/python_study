import sys

while True:
    s = sys.stdin.readline().rstrip('\n')
    a=0 #소문자
    b=0 #대문자
    c=0 #숫자
    d=0 #공백
    
    if not s:
        break
    for i in s:
        if i.isupper():
            b+=1
        elif i.islower():
            a+=1
        elif i.isdigit():
            c+=1
        elif i.isspace():
            d+=1

    print('%d %d %d %d'%(a, b, c, d))