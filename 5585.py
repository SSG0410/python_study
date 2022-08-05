n = int(input())
list = [500,100,50,10,5,1]
ans = 0
money = 1000-n
for i in list:
    ans += money//i
    money = money%i

print(ans)