import sys
from collections import deque
input = sys.stdin.readline

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def bfs1():
    global cnt1
    cnt1 += 1
    while queue:
        y, x = queue.popleft()
        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]
            if 0 <= ny < n and 0 <= nx < n and not visited1[ny][nx]:
                if board[y][x] == board[ny][nx]:
                    queue.append((ny, nx))
                    visited1[ny][nx] = True


def bfs2():
    global cnt2
    cnt2 += 1
    while queue:
        y, x = queue.popleft()
        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]
            if 0 <= ny < n and 0 <= nx < n and not visited2[ny][nx]:
                if board[y][x] == board[ny][nx]:
                    queue.append((ny, nx))
                    visited2[ny][nx] = True
                elif board[y][x] == 'R' or board[y][x] == 'G':
                    if board[ny][nx] == 'R' or board[ny][nx] == 'G':
                        queue.append((ny, nx))
                        visited2[ny][nx] = True


queue = deque()
n = int(input())
board = [list(input().rstrip()) for _ in range(n)]
visited1 = [[False] * n for _ in range(n)]
visited2 = [[False] * n for _ in range(n)]
cnt1 = 0
cnt2 = 0

for y in range(n):
    for x in range(n):
        if not visited1[y][x]:
            queue.append((y, x))
            visited1[y][x] = True
            bfs1()

for y in range(n):
    for x in range(n):
        if not visited2[y][x]:
            queue.append((y, x))
            visited2[y][x] = True
            bfs2()


print(cnt1, cnt2)
