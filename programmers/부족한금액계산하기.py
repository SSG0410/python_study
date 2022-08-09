def solution(price, money, count):
    if count%2==0:
        moneysum = ((1+count)*(count//2))*price
    else:
        moneysum = (((1+count)*(count//2))+((count+1)//2))*price
    if moneysum>money:
        return moneysum-money
    else:
        return 0
