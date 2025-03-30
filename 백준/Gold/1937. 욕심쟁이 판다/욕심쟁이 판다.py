import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
dp = [[-1 for _ in range(n)] for _ in range(n)]
ans = 1

def dfs(y,  x):
    global ans
    # 이미 방문했으면 해당 지점의 dp값 리턴
    if dp[y][x] != -1:
        return dp[y][x]
    # 방문 체크
    dp[y][x] = 1
    for k in range(4):
        ny = y + dy[k]
        nx = x + dx[k]
        if 0 <= ny < n and 0 <= nx < n:
            if board[y][x] < board[ny][nx]:
                cnt = 1 + dfs(ny, nx)
                dp[y][x] = max(dp[y][x], cnt)
                ans = max(ans, dp[y][x])
    return dp[y][x]

for y in range(n):
    for x in range(n):
        if dp[y][x] == -1:
            dfs(y, x)
print(ans)