import sys
from collections import deque

input = sys.stdin.readline
queue = deque()
m, n, h = map(int, input().split())

tomatoes = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]
visited = [[[False] * m for _ in range(n)] for _ in range(h)]

cnt = 0
dx = [1, 0, -1, 0, 0, 0]
dy = [0, -1, 0, 1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]


def bfs():
    global day
    while queue:
        ez, ey, ex = queue.popleft()
        for k in range(6):
            nz = ez + dz[k]
            ny = ey + dy[k]
            nx = ex + dx[k]
            if 0 <= nz < h and 0 <= ny < n and 0 <= nx < m:
                if tomatoes[nz][ny][nx] == 0:
                    tomatoes[nz][ny][nx] = tomatoes[ez][ey][ex] + 1
                    queue.append((nz, ny, nx))
                    if day < tomatoes[nz][ny][nx]:
                        day = tomatoes[nz][ny][nx] - 1


for z in range(h):
    for y in range(n):
        for x in range(m):
            if tomatoes[z][y][x] == 1:
                queue.append((z, y, x))

day = 0
bfs()

for z in range(h):
    for y in range(n):
        if 0 in tomatoes[z][y]:
            print(-1)
            exit()
        if z == h-1 and y == n-1:
            print(day)





