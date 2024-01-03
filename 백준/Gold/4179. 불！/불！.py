import sys
from collections import deque

input = sys.stdin.readline

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def bfs():
    while queue:
        y, x = queue.popleft()
        flag = visited[y][x]
        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]
            if 0 <= ny < r and 0 <= nx < c:
                if visited[ny][nx] == - 1 and (board[ny][nx] == "." or board[ny][nx] == "J"):
                    if flag == "FIRE":
                        visited[ny][nx] = flag
                    else:
                        visited[ny][nx] = visited[y][x] + 1
                    queue.append((ny, nx))
            else:
                if flag != "FIRE":
                    return visited[y][x] + 1
    return "IMPOSSIBLE"


r, c = map(int, input().split())
queue = deque()
board = []
visited = [[-1] * c for _ in range(r)]
for y in range(r):
    board.append(list(input().strip()))
    for x in range(c):
        if board[y][x] == "J":
            visited[y][x] = 0
            start = (y, x)
        elif board[y][x] == "F":
            visited[y][x] = "FIRE"
            queue.append((y,x))
queue.append(start)
print(bfs())
