import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
nodes = [[] for _ in range(n + 1)]
parent = [0] * (n + 1)

for __ in range(n - 1):
    s, e = map(int, input().split())
    nodes[s].append(e)
    nodes[e].append(s)

q = deque([1])
while q:
    current = q.popleft()
    for node in nodes[current]:
        if parent[node] == 0:
            parent[node] = current
            q.append(node)

print('\n'.join(map(str, parent[2:])))