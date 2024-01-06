import sys
from collections import deque

input = sys.stdin.readline

def bfs():
    while queue:
        n, cnt = queue.popleft()
        if n == k:
            return cnt
        else:
            if 0 <= n * 2 <= max and not visited[n * 2]:
                queue.append((n * 2, cnt))
                visited[n * 2] = True
            if 0 <= n - 1 <= max and not visited[n - 1]:
                queue.append((n - 1, cnt + 1))
                visited[n - 1] = True
            if 0 <= n + 1 <= max and not visited[n + 1]:
                queue.append((n + 1, cnt + 1))
                visited[n + 1] = True


n, k = map(int, input().split())
cnt = 0
queue = deque([(n, cnt)])
max = 10 ** 5
visited = [False] * (max + 1)
visited[n] = True
print(bfs())
