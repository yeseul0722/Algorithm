import sys
from collections import deque

input = sys.stdin.readline

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def bfs():
    while queue:
        y, x = queue.popleft()
        if visited[y][x] != "FIRE":
            flag = visited[y][x]
        else:
            flag = "FIRE"
        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]
            if 0 <= ny < h and 0 <= nx < w:
                if visited[ny][nx] == -1 and (board[ny][nx] == "." or board[ny][nx] == "@"):
                    if flag == "FIRE":
                        visited[ny][nx] = flag
                    else:
                        visited[ny][nx] = flag + 1
                    queue.append((ny, nx))
            else:
                if flag != "FIRE":
                    return flag + 1
    return "IMPOSSIBLE"

t = int(input())
for _ in range(t):
    w, h = map(int, input().split())
    queue = deque()
    board = []
    visited = [[-1] * w for _ in range(h)]
    for y in range(h):
        board.append(list(input().strip()))
        for x in range(w):
            if board[y][x] == "@":
                visited[y][x] = 0
                start = (y, x)
            elif board[y][x] == "*":
                visited[y][x] = "FIRE"
                queue.append((y, x))
    queue.append(start)
    print(bfs())