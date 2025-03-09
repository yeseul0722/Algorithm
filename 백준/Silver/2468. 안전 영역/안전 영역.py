from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
mat = []
max_num = 0

for i in range(N):
    data = (list(map(int, input().split())))
    mat.append(data)

for i in range(N):
    for j in range(N):
        if mat[i][j] > max_num:
            max_num = mat[i][j]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def bfs(a, b, value, visited):
    q = deque()
    q.append((a, b))
    visited[a][b] = 1

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if mat[nx][ny] > value and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    q.append((nx, ny))


result = 0
for i in range(max_num):
    visited = [[0] * N for _ in range(N)]
    cnt = 0
    for j in range(N):
        for k in range(N):
            if mat[j][k] > i and visited[j][k] == 0:
                bfs(j, k, i, visited)
                cnt += 1

    if cnt > result:
        result = cnt

print(result)
