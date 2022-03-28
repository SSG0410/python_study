a, b = map(int, input().split())
tempa=a
tempb=b
while tempb!=0:
    tempa=tempa%tempb
    tempa,tempb=tempb,tempa

print(tempa)
print(a*b//tempa)