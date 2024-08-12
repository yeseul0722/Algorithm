def solution(arr):
    n = len(arr)
    answer = [0, 0]
    
    def press(start, end, n):
        temp = arr[start][end]
        for i in range(start, start + n):
            for j in range(end, end + n):
                if arr[i][j] != temp:
                    n //= 2
                    press(start, end, n)
                    press(start, end + n, n)
                    press(start + n, end, n)
                    press(start + n, end + n, n)
                    return
        answer[temp] += 1
    
    press(0, 0, n)
    
    return answer