import sys
import copy
from collections import deque
input = sys.stdin.readline

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def bfs():
    global ans
    queue = deque()
    temp_board = copy.deepcopy(board)

    for y in range(n):
        for x in range(m):
            if temp_board[y][x] == 2:
                queue.append((y, x))

    while queue:
        y, x = queue.popleft()

        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]
            if 0 <= ny < n and 0 <= nx < m and temp_board[ny][nx] == 0:
                temp_board[ny][nx] = 2
                queue.append((ny, nx))
    cnt = 0
    for y in range(n):
        for x in range(m):
            if temp_board[y][x] == 0:
                cnt += 1
    ans = max(cnt, ans)


def dfs(num):
    if num == 3:
        bfs()
        return

    for y in range(n):
        for x in range(m):
            if board[y][x] == 0:
                board[y][x] = 1
                dfs(num + 1)
                board[y][x] = 0


n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
ans = 0
dfs(0)
print(ans)