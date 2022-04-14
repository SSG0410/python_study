day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
week = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
x, y = map(int, input().split())

#1 1=월요일
if x==1:
    print(week[(y-1)%7])
else:
    for i in range(x-1):
        y += day[i]
    print(week[(y-1)%7])