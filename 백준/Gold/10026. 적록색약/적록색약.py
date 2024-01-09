import sys
sys.setrecursionlimit(10**6) # 파이썬의 재귀 깊이 지정 (Python3)
input = sys.stdin.readline
N = int(input())

graph = []
visited = [[0] * (N) for _ in range(N)]
sum = 0
sum2 = 0

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

for i in range(N):
    graph.append(list(input()))

def dfs(x, y, color):
    visited[x][y] = 1

    # 동서남북 탐색
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 범위 내에 있고 방문한 적이 없다면
        if 0 <= nx <= N-1 and 0 <= ny <= N-1 and visited[nx][ny] == 0:
            # 위 조건을 모두 만족하면서 탐색중인 색상과 같은 색상이면 탐색
            if graph[nx][ny] == color:
                dfs(nx, ny, color)

for color in ['R','G','B']: # 빨->초->파 순서로 확인
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0 and graph[i][j] == color:
                dfs(i, j,color)
                sum += 1

# 기존 그래프에서 초록색 -> 빨간색으로 변경
for i in range(N):
    for j in range(N):
        if graph[i][j] == 'G':
            graph[i][j] = 'R'

# 방문 정보 초기화
visited = [[0] * (N) for _ in range(N)]

for color in ['R', 'B']: # 빨,파만 확인
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0 and graph[i][j] == color:
                dfs(i, j,color)
                sum2 += 1

print(sum, sum2)