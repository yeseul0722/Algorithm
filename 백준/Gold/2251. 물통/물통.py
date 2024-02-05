import sys
from collections import deque
input = sys.stdin.readline
queue = deque()
queue.append((0, 0))

a, b, c = map(int, input().split())
visited = [[False] * (b + 1) for _ in range(a + 1)]
visited[0][0] = True

ans = []


def pour(x, y):
    if not visited[x][y]:
        visited[x][y] = True
        queue.append((x, y))
        
        
def bfs():
    while queue:
        x, y = queue.popleft()
        z = c - x - y
        
        if x == 0:
            ans.append(z)

        water = min(x, b - y)
        pour(x - water, y + water)
        water = min(x, c - z)
        pour(x - water, y)
        
        water = min(y, c - z)
        pour(x, y - water)
        water = min(y, a - x)
        pour(x + water, y - water)
        
        water = min(z, a - x)
        pour(x + water, y)
        water = min(z, b - y)
        pour(x, y + water)
     
        
bfs()

ans.sort()
for i in ans:
    print(i, end=" ")
