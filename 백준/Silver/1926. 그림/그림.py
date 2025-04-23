import sys
from collections import deque

input = sys.stdin.readline

def bfs(now):
    q = deque([now])
    tmp = 1
    while q:
        y, x = q.popleft()
        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]
            if 0 <= ny < n and 0 <= nx < m:
                if not visited[ny][nx] and board[ny][nx] == 1:
                    visited[ny][nx] = True
                    tmp += 1
                    q.append([ny, nx])
    return tmp

board = []
ans = []
dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

n, m = map(int, input().split())
for _ in range(n):
    board.append(list(map(int, input().split())))

visited = [[False] * m for _ in range(n)]

for y in range(n):
    for x in range(m):
        if not visited[y][x] and board[y][x] == 1:
            visited[y][x] = True
            cnt = bfs([y, x])
            ans.append(cnt)

print(len(ans))
if not ans:
    print(0)
else:
    print(max(ans))