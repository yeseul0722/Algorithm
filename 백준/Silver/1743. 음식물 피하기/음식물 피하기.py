import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

n, m, k = map(int, input().split())
board = [[0] * m for _ in range(n)]
visited = [[False] * m for _ in range(n)]
result = []
temp = 0

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

def dfs(y, x):
    global temp
    temp += 1
    for k in range(4):
        ny = y + dy[k]
        nx = x + dx[k]
        if 0 <= ny < n and 0 <= nx < m and not visited[ny][nx]:
            visited[ny][nx] = True
            if board[ny][nx] == 1:
                dfs(ny, nx)

for _ in range(k):
    r, c = map(int, input().split())
    board[r - 1][c - 1] = 1

for y in range(n):
    for x in range(m):
        if board[y][x] == 1 and not visited[y][x]:
            temp = 0
            visited[y][x] = True
            dfs(y, x)
            result.append(temp)

print(max(result))