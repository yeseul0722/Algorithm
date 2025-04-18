import math
import sys
from collections import deque
input = sys.stdin.readline

def bfs(now):
    q = deque([now])
    cnt = 0
    while q:
        v, usado = q.popleft()
        for nv, nusado in node[v]:
            nusado = min(usado, nusado)
            if nusado >= k and not visited[nv]:
                cnt += 1
                q.append((nv, nusado))
                visited[nv] = True
    return cnt

n, q = map(int, input().split())
node = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    a, b, usado = map(int, input().split())
    node[a].append((b, usado))
    node[b].append((a, usado))

for _ in range(q):
    k, v = map(int, input().split())
    visited = [False] * (n + 1)
    visited[v] = True
    print(bfs((v, math.inf)))
