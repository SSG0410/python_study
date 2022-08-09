def solution(sizes):
    answer = 0
    x_max = 0
    y_max = 0
    
    for i in range(len(sizes)):
        tmp_max = max(sizes[i][0],sizes[i][1])
        tmp_min = min(sizes[i][0],sizes[i][1])
        if x_max<tmp_max:
            x_max = tmp_max
        if y_max<tmp_min:
            y_max = tmp_min
    
    answer = x_max * y_max
    
    return answer
