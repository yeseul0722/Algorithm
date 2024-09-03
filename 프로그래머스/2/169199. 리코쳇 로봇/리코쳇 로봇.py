import sys
from collections import deque
def solution(board):
    
    max_num = sys.maxsize
    m = len(board[0])
    n = len(board)
    visited = [[max_num] * m for _ in range(n)]
    dy = [1, 0, -1, 0]
    dx = [0, 1, 0, -1]
    
    for y in range(n):
        for x in range(m):
            if board[y][x] == 'R':
                sy, sx = y, x
            if board[y][x] == 'G':
                gy, gx = y, x
                
    visited[sy][sx] = 0
    queue = deque([(sy, sx)])
    while queue:
        y, x = queue.popleft()
        for i in range(4):
            ny, nx = y, x
            while 0 <= ny + dy[i] < n and 0 <= nx + dx[i] < m and board[ny + dy[i]][nx + dx[i]] != 'D':
                ny += dy[i]
                nx += dx[i]
            
            if visited[y][x] + 1 < visited[ny][nx]:
                visited[ny][nx] = visited[y][x] + 1
                queue.append((ny, nx))
                
            if(ny, nx) == (gy, gx):
                    for row in visited:
                        print(row)
                    return visited[y][x] + 1
                  
    return -1