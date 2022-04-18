while True:
    n = list(input())
    reverse_n = n[::-1]

    if n==['0']:
        break

    if n==reverse_n:
        print('yes')
    else:
        print('no')