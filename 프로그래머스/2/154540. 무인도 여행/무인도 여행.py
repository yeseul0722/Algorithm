from collections import deque
def solution(maps):
    answer = []
    n = len(maps[0])
    m = len(maps)
    visited = [[False] * n for _ in range(m)]
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    
    def bfs(y, x):
        queue = deque([(y, x)])
        sum = 0
        visited[y][x] = True
        while queue:
            y, x = queue.popleft()
            sum += int(maps[y][x])
            print(y, x, maps[y][x], sum)
            for k in range(4):
                ny = y + dy[k]
                nx = x + dx[k]
                
                if 0 <= ny < m and 0 <= nx < n and not visited[ny][nx] and maps[ny][nx] != 'X':
                    visited[ny][nx] = True
                    queue.append((ny, nx))
        return sum
    
    for y in range(m):
        for x in range(n):
            if not visited[y][x] and maps[y][x] != 'X':
                answer.append(bfs(y, x))
    
    if len(answer) == 0:
        answer.append(-1)
        
    answer.sort()
    return answer