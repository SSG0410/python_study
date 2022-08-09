def solution(x):
    tmp = list(map(int,str(x)))
    if x%sum(tmp)==0:
        return True
    else:
        return False
