import sys
from collections import deque
def solution(board):
    dy = [1, 0, -1, 0]
    dx = [0, 1, 0, -1]
    n = len(board)
    m = len(board[0])
    max_num = sys.maxsize
    visited = [[max_num] * m for _ in range(n)]
    
    for y in range(n):
        for x in range(m):
            if board[y][x] == 'R':
                sy, sx = y, x
            if board[y][x] == 'G':
                gy, gx = y, x
                
    queue = deque([(sy, sx)])
    visited[sy][sx] = 0
    
    while queue:
        y, x = queue.popleft()
        for i in range(4):
            ny, nx = y, x
            while 0 <= ny + dy[i] < n and 0 <= nx + dx[i] < m and board[ny + dy[i]][nx + dx[i]] != 'D':
                ny += dy[i]
                nx += dx[i]
                
            if visited[ny][nx] > visited[y][x] + 1:
                visited[ny][nx] = visited[y][x] + 1
                queue.append((ny, nx))
                
            if (ny, nx) == (gy, gx):
                return visited[ny][nx]
    
    return -1