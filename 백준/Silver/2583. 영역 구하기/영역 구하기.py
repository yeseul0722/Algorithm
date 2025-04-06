import sys

input = sys.stdin.readline
from collections import deque

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def bfs(now):
    q = deque(now)
    tmp_width = 0
    while q:
        y, x = q.popleft()
        board[y][x] = 1
        tmp_width += 1
        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]
            if 0 <= ny < m and 0 <= nx < n and board[ny][nx] == 0:
                q.append([ny, nx])
                board[ny][nx] = 1
    return tmp_width


m, n, k = map(int, input().split())
board = [[0] * n for _ in range(m)]
width_lst = []
cnt = 0

for _ in range(k):
    lx, ly, rx, ry = map(int, input().split())
    for y in range(ly, ry):
        for x in range(lx, rx):
            board[y][x] = 1

for y in range(m):
    for x in range(n):
        if board[y][x] == 0:
            width = bfs([[y, x]])
            width_lst.append(width)
            cnt += 1

width_lst.sort()
print(cnt)
print(' '.join(map(str, width_lst)))
