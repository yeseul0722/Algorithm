import sys
input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(input().strip()) for _ in range(m)]
visited = [[False] * n for _ in range(m)]
w = []
b = []
dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]
temp = 0


def dfs(y, x):
    global temp
    temp += 1
    for k in range(4):
        ny = y + dy[k]
        nx = x + dx[k]
        if 0 <= ny < m and 0 <= nx < n:
            if not visited[ny][nx] and board[ny][nx] == board[y][x]:
                visited[ny][nx] = True
                dfs(ny, nx)


for y in range(m):
    for x in range(n):
        if not visited[y][x]:
            visited[y][x] = True
            temp = 0
            dfs(y, x)
            if board[y][x] == "W":
                w.append(temp ** 2)
            else:
                b.append(temp ** 2)


print(sum(w), sum(b))
