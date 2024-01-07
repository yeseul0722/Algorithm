# 북 동 남 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def simulator(y, x, d):
    global dx, dy
    cnt = 1
    visited[y][x] = 1
    while True:
        flag = 0
        for _ in range(4):
            d = (d + 3) % 4
            ny = y + dx[d]
            nx = x + dy[d]
            if 0 <= ny < n and 0 <= nx < m:
                if board[ny][nx] == 0 and visited[ny][nx] == 0:
                    visited[ny][nx] = 1
                    y, x = ny, nx
                    cnt += 1
                    flag = 1
                    break

        if flag == 0:
            if board[y - dx[d]][x - dy[d]] == 1:
                return cnt
            else:
                y, x = y - dx[d], x - dy[d]


n, m = map(int, input().split())
r, c, d = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
print(simulator(r, c, d))
