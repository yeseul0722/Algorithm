import sys
from collections import deque
input = sys.stdin.readline


dy = [1, 0, -1, 0]
dx = [0, -1, 0, 1]


def bfs():
    cnt = 0
    queue = deque()
    queue.append((0, 0))
    visited[0][0] = True
    while queue:
        y, x = queue.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < n and 0 <= nx < m and not visited[ny][nx]:
                if board[ny][nx] == 0:
                    visited[ny][nx] = True
                    queue.append((ny, nx))
                else:
                    board[ny][nx] = 0
                    visited[ny][nx] = True
                    cnt += 1

    ans.append(cnt)
    return cnt


n, m = map(int, input().split())
board = []
ans = []
for _ in range(n):
    data = list(map(int, input().split()))
    board.append(data)

time = 0
while True:
    time += 1
    visited = [[False] * m for _ in range(n)]
    cnt = bfs()
    if cnt == 0:
        break

print(time - 1)
print(ans[-2])