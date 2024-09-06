def solution(arr):
    answer = [0, 0]
    n = len(arr)
    
    def press(y, x, n):
        temp = arr[y][x]
        for i in range(y, y + n):
            for j in range(x, x + n):
                if arr[i][j] != temp:
                    n //= 2
                    press(y, x, n)
                    press(y, x + n, n)
                    press(y + n, x, n)
                    press(y + n, x + n, n)
                    return
        answer[temp] += 1
    press(0, 0, n)
    
    return answer