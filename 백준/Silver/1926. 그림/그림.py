import sys
input = sys.stdin.readline

n, m = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for __ in range(n)]

cnt = 0
max_num = 0

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]
def bfs(y, x):
    size = 1
    q = [(y, x)]
    while q:
        ey, ex = q.pop(0)
        for k in range(4):
            ny = ey + dy[k]
            nx = ex + dx[k]
            if 0 <= ny < n and 0 <= nx < m:
                if map[ny][nx] == 1 and visited[ny][nx] == False:
                    visited[ny][nx] = True
                    q.append((ny, nx))
                    size += 1
    return size


for j in range(n):
    for i in range(m):
        if map[j][i] == 1 and visited[j][i] == False:
            cnt += 1
            visited[j][i] = True
            max_num = max(max_num, bfs(j, i))


print(cnt)
print(max_num)