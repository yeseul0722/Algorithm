import sys
input = sys.stdin.readline

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

def bfs(y, x):
    q = [(y, x)]
    while q:
        ey, ex = q.pop(0)
        for k in range(4):
            ny = ey + dy[k]
            nx = ex + dx[k]
            if 0 <= ny < n and 0 <= nx < m:
                if graph[ny][nx] == 1 and visited[ny][nx] == False:
                    visited[ny][nx] = True
                    q.append((ny, nx))



T = int(input())
for _ in range(T):
    m, n, k = map(int, input().split())
    cnt = 0
    graph = [[0] * m for _ in range(n)]
    visited = [[False] * m for _ in range(n)]
    for _ in range(k):
        x, y = map(int, input().split())
        graph[y][x] = 1

    for j in range(n):
        for i in range(m):
            if graph[j][i] == 1 and visited[j][i] == False:
                visited[j][i] = True
                cnt += 1
                bfs(j, i)

    print(cnt)
