import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(N + 1)]
for _ in range(M):
    A, B = map(int, sys.stdin.readline().split())
    graph[B].append(A)

def BFS(v):
    visited[v] = False
    queue = deque()
    queue.append(v)

    while (queue):
        now = queue.popleft()
        for i in graph[now]:
            if (visited[i]):
                queue.append(i)
                visited[i] = False

    return visited.count(False)

result = [0] * (N + 1)
for i in range(1, N + 1):
    visited = [True] * (N + 1)
    result[i] = BFS(i)

MAX = max(result)
for i in range(1, N + 1):
    if (result[i] == MAX):
        print(i, end=' ')