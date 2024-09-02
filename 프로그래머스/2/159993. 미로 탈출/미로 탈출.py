from collections import deque
def solution(maps):
    n = len(maps)
    m = len(maps[0])
    
    def bfs(S, G):
        dy = [1, 0, -1, 0]
        dx = [0, 1, 0, -1]
        visited = [[-1] * m for _ in range(n)]
        queue = deque()
        
        for y in range(n):
            for x in range(m):
                if maps[y][x] == S:
                    queue.append((y, x))
                    visited[y][x] = 0
                    break

        while queue:
            y, x = queue.popleft()
            if maps[y][x] == G:
                return visited[y][x]
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                if 0 <= ny < n and 0 <= nx < m and visited[ny][nx] == -1 and not maps[ny][nx] == 'X':
                    queue.append((ny, nx))
                    visited[ny][nx] = visited[y][x] + 1
        return -1
    
    flag1 = bfs('S', 'L')
    flag2 = bfs('L', 'E')
    if flag1 != -1 and flag2 != -1:
        return flag1 + flag2
    else:
        return -1

    