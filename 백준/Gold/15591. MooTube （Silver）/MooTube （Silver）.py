import math
import sys
from collections import deque
input = sys.stdin.readline

def bfs(start):
    q = deque([start])
    cnt = 0
    while q:
        v = q.popleft()
        for nv, nusado in node[v]:
            if not visited[nv] and nusado >= k:
                cnt += 1
                q.append(nv)
                visited[nv] = True
    return cnt

n, q = map(int, input().split())
node = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    a, b, usado = map(int, input().split())
    node[a].append([b, usado])
    node[b].append([a, usado])

for _ in range(q):
    k, v = map(int, input().split())
    visited = [False] * (n + 1)
    visited[v] = True
    print(bfs(v))
