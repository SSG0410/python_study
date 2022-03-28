n = int(input())
for i in range(n):
    a, b = map(int, input().split())

    new_a = a
    new_b = b
    while new_b != 0:
        new_a = new_a % new_b
        new_a, new_b = new_b, new_a
    
    최대공약수=new_a

    최소공배수=a*b//최대공약수
    print(최소공배수)