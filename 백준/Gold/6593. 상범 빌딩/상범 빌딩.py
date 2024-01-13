import sys
from collections import deque

input = sys.stdin.readline

dx = [1, 0, -1, 0, 0, 0]
dy = [0, 1, 0, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]


def bfs():
    while queue:
        z, y, x = queue.popleft()
        for k in range(6):
            nz = z + dz[k]
            ny = y + dy[k]
            nx = x + dx[k]
            if 0 <= nz < l and 0 <= ny < r and 0 <= nx < c:
                if (board[nz][ny][nx] == '.' or board[nz][ny][nx] == 'E') and visited[nz][ny][nx] == -1:
                    queue.append((nz, ny, nx))
                    visited[nz][ny][nx] = visited[z][y][x] + 1
                    if board[nz][ny][nx] == 'E':
                        return visited[nz][ny][nx]
    return -1


while True:
    l, r, c = map(int, input().split())
    time = 0
    queue = deque()
    if l == 0 and r == 0 and c == 0:
        break
    board = []
    visited = [[[-1] * c for _ in range(r)]for _ in range(l)]
    for _ in range(l):
        board.append([list(input().rstrip()) for _ in range(r)])
        input()

    for z in range(l):
        for y in range(r):
            for x in range(c):
                if board[z][y][x] == 'S':
                    queue.append((z, y, x))
                    visited[z][y][x] = 0
                    time = bfs()

    if time > 0:
        print(f'Escaped in {time} minute(s).')
    else:
        print('Trapped!')

