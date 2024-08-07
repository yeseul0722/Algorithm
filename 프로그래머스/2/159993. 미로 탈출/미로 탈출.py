from collections import deque

def bfs(start, end, maps):
    queue = deque()
    n = len(maps[0])
    m = len(maps)
    visited = [[-1] * n for _ in range(m)]
    flag = False
    
    dy = [1, 0, -1, 0]
    dx = [0, 1, 0, -1]
    
    for y in range(m):
        for x in range(n):
            if maps[y][x] == start:
                queue.append((y, x))
                visited[y][x] = 0
                break
    
    while queue:
        y, x = queue.popleft()
        if maps[y][x] == end:
            return visited[y][x]
        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]
            if 0 <= nx < n and 0 <= ny < m and visited[ny][nx] == -1 and maps[ny][nx] != 'X':
                visited[ny][nx] = visited[y][x] + 1
                queue.append((ny, nx))
    return -1       

def solution(maps):
    path1 = bfs('S', 'L', maps)
    path2 = bfs('L', 'E', maps)
    if path1 != -1 and path2 != -1:
        return path1 + path2
    else:
        return -1
