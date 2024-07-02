from collections import deque
def solution(maps):
    n = len(maps[0])
    m = len(maps)
    
    dy = [1, 0, -1, 0]
    dx = [0, 1, 0, -1]
    visited = [[-1] * n for _ in range(m)]
    queue = deque([(0, 0)])
    
    while queue:
        y, x = queue.popleft()
        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]
            if 0 <= ny < m and 0 <= nx < n and visited[ny][nx] == -1 and maps[ny][nx]:
                queue.append((ny, nx))
                visited[ny][nx] = visited[y][x] + 1
    
    answer = visited[m - 1][n - 1]
    if answer != -1:
        answer += 2
                
    return answer