import sys
from collections import deque
def solution(board):
    answer = 0
    max_num = sys.maxsize
    print(max_num)
    m = len(board[0])
    n = len(board)
    visited = [[-1] * m for _ in range(n)]
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
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < n and 0 <= nx < m and visited[ny][nx] == -1 and not board[ny][nx] == 'D':
                visited[ny][nx] = visited[y][x] + 1
                queue.append((ny, nx))
    
    for row in visited:
        print(row)
    return visited[gy][gx]