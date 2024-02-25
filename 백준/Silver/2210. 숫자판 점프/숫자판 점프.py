import sys
input = sys.stdin.readline


dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]


def dfs(y, x, number):
    if len(number) == 6:
        ans.append(number)
        return

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < 5 and 0 <= nx < 5:
            dfs(ny, nx, number + board[ny][nx])


board = [list(map(str, input().split())) for _ in range(5)]
ans = []
for y in range(5):
    for x in range(5):
        dfs(y, x, board[y][x])

print(len(set(ans)))