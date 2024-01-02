import sys
from collections import deque
input = sys.stdin.readline

def bfs(start):
    num = [0] * (n + 1)
    visited = [start]
    queue = deque()
    queue.append(start)

    while queue:
        a = queue.popleft()
        for k in friends[a]:
            if k not in visited:
                num[k] = num[a] + 1
                visited.append(k)
                queue.append(k)
    return sum(num)


n, m = map(int, input().split())
friends = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    friends[a].append(b)
    friends[b].append(a)

result = []

for i in range(1, n + 1):
    result.append(bfs(i))

print(result.index(min(result))+ 1)