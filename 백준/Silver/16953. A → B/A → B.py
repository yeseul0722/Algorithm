import sys
from collections import deque

input = sys.stdin.readline
queue = deque()

def bfs(a, b):
    queue = deque([(a, 1)])
    while queue:
        a, cnt = queue.popleft()
        if a == b:
            print(cnt)
            return

        if a * 2 <= b:
            queue.append((a * 2, cnt + 1))
        if a * 10 + 1 <= b:
            queue.append((a * 10 + 1, cnt + 1))
    print(-1)

a, b = map(int, input().split())
bfs(a, b)