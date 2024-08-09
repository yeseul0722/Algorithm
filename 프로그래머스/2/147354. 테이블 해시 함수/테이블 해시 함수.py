def solution(data, col, row_begin, row_end):
    answer = 0
    data.sort(key = lambda x : [x[col - 1], -x[0]])
    
    for i in range(row_begin - 1, row_end):
        sum = 0
        for j in range(len(data[i])):
            sum += data[i][j] % (i + 1)
        answer ^= sum
        
    return answer