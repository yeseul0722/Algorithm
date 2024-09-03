def solution(board):
    n = len(board)
    m = len(board[0])
    dp = [[0] * m for _ in range(n)]
    dp[0] = board[0]
    
    for i in range(n):
        dp[i][0] = board[i][0]
        
    for y in range(1, n):
        for x in range(1, m):
            if board[y][x] == 1:
                dp[y][x] = min(dp[y - 1][x - 1], dp[y - 1][x], dp[y][x - 1]) + 1
    
    answer = 0
    for i in range(n):
        temp = max(dp[i])
        answer = max(answer, temp)

    return answer ** 2