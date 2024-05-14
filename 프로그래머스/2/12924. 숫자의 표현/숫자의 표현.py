def solution(n):
    answer = 0
    start, end = 1, 1
    sum_num = start

    while end < n + 1:
        if sum_num >= n:
            if sum_num == n:
                answer += 1
            sum_num -= start
            start += 1
        else:
            end += 1
            sum_num += end

    return answer