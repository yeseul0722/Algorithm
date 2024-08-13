import sys
from collections import deque

input = sys.stdin.readline
n, k = map(int, input().split())
answer = 0
max_num = 10 ** 5
visited = [0] * (max_num + 1)

def bfs():
    queue = deque(([n]))
    while queue:
        x = queue.popleft()
        if x == k:
            print(visited[k])
            return
        for nx in (x - 1, x + 1, x * 2):
            if 0 <= nx <= max_num and not visited[nx]:
                visited[nx] = visited[x] + 1
                queue.append(nx)

bfs()