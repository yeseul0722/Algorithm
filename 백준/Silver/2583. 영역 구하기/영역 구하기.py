import sys
from collections import deque

input = sys.stdin.readline
queue = deque()

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def bfs():
    global temp
    while queue:
        y, x = queue.popleft()
        temp += 1
        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]
            if 0 <= ny < m and 0 <= nx < n and not visited[ny][nx]:
                if maze[ny][nx] == 0:
                    visited[ny][nx] = True
                    queue.append((ny, nx))
    if temp <= 1:
        return temp
    else:
        return temp - 1


m, n, k = map(int, input().split())
maze = [[0] * n for _ in range(m)]
visited = [[False] * n for _ in range(m)]
cnt = 0
width = []
for _ in range(k):
    sx, sy, ex, ey = map(int, input().split())
    for y in range(sy, ey):
        for x in range(sx, ex):
            maze[y][x] = 1


for y in range(m):
    for x in range(n):
        temp = 0
        if maze[y][x] == 0 and not visited[y][x]:
            queue.append((y, x))
            temp = bfs()
            cnt += 1
            if temp > 0:
                width.append(temp)

width.sort()
print(cnt)
print(*width)

