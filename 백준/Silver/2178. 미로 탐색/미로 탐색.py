from collections import deque

N, M = map(int, input().split())
maze = []
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

for __ in range(N):
    data = list(map(int, input().rstrip()))
    maze.append(data)

def bfs(y, x):
    queue = deque()
    queue.append([y, x])
    while queue:
        y, x = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < M and 0 <= ny < N and maze[ny][nx] == 1:
                queue.append([ny, nx])
                maze[ny][nx] = maze[y][x] + 1
                if nx == M - 1 and ny == N - 1:
                    return maze[y][x] + 1


print(bfs(0, 0))