from collections import deque
import sys
input = sys.stdin.readline

n, m, v = map(int, input().split())
node = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    node[a].append(b)
    node[b].append(a)

for k in node:
    k.sort()

visited_dfs = [False] * (n + 1)

def dfs(v):
    print(v, end=' ')
    visited_dfs[v] = True
    for i in node[v]:
        if not visited_dfs[i]:
            dfs(i)


def bfs(v):
    queue = deque([v])
    visited = [False] * (n + 1)
    visited[v] = True
    while queue:
        now = queue.popleft()
        print(now, end=' ')
        for i in node[now]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


dfs(v)
print()
bfs(v)