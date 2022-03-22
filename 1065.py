def get_hansu(n):
    if n<100:
        hansu=n
    else:
        hansu=99 #1~99까지의 한수 99개
        for i in range(100,n+1):
            num_list=list(map(int, str(i)))
            if num_list[2]-num_list[1]==num_list[1]-num_list[0]:
                hansu+=1
    return hansu
        

num = int(input())
print(get_hansu(num))