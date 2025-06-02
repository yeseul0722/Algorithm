import sys
from collections import deque
input = sys.stdin.readline

dy = [-1, -1, 0, 1, 1, 1, 0, -1]
dx = [0, 1, 1, 1, 0, -1, -1, -1]

def bfs():
    queue = deque(shark)

    while queue:
        y, x = queue.popleft()
        for k in range(8):
            ny = y + dy[k]
            nx = x + dx[k]
            if 0 <= ny < n and 0 <= nx < m:
                if not board[ny][nx]:
                    queue.append([ny, nx])
                    board[ny][nx] = board[y][x] + 1


n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
shark = []
ans = 0
for y in range(n):
    for x in range(m):
        if board[y][x] == 1:
            shark.append(([y, x]))

bfs()

for y in range(n):
    for x in range(m):
        ans = max(ans, board[y][x])

print(ans - 1)