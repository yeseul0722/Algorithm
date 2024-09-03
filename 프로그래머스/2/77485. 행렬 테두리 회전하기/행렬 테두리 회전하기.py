def solution(rows, columns, queries):
    answer = []
    board = [[0] * columns for _ in range(rows)]
    
    cnt = 1
    for y in range(rows):
        for x in range(columns):
            board[y][x] = cnt
            cnt += 1
    
    for x1, y1, x2, y2 in queries:
        origin = board[x1 - 1][y1 - 1]
        min_num = origin
        
        for i in range(x1 - 1, x2 - 1):
            temp = board[i + 1][y1 - 1]
            board[i][y1 - 1] = temp
            min_num = min(min_num, temp)
            
        for i in range(y1 - 1, y2 - 1):
            temp = board[x2 - 1][i + 1]
            board[x2 - 1][i] = temp
            min_num = min(min_num, temp)
            
        for i in range(x2 - 1, x1 - 1, -1):
            temp = board[i - 1][y2 - 1]
            board[i][y2 - 1] = temp
            min_num = min(min_num, temp)
            
        for i in range(y2 - 1, y1 - 1, -1):
            temp = board[x1 - 1][i - 1]
            board[x1 - 1][i] = temp
            min_num = min(min_num, temp)
            
        board[x1 - 1][y1] = origin
        answer.append(min_num)
        
    return answer