import sys
from collections import deque

input = sys.stdin.readline


def bfs(now):
    q = deque([now])
    size = 1
    while q:
        y, x = q.popleft()
        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]
            if 0 <= ny < n and 0 <= nx < m:
                if not visited[ny][nx] and board[ny][nx] == 1:
                    visited[ny][nx] = True
                    size += 1
                    q.append([ny, nx])
    return size


board = []
cnt = 0
max_num = 0
dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

visited = [[False] * m for _ in range(n)]

for y in range(n):
    for x in range(m):
        if not visited[y][x] and board[y][x] == 1:
            visited[y][x] = True
            cnt += 1
            max_num =  max(bfs([y, x]), max_num)

print(cnt)
print(max_num)
