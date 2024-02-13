import sys
from collections import deque
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    queue = deque(list(map(int, input().split())))
    cnt = 0
    while queue:
        max_num = max(queue)
        front = queue.popleft()
        m -= 1
        
        if max_num == front:
            cnt += 1
            if m < 0:
                print(cnt)
                break
        else:
            queue.append(front)
            if m < 0:
                m = len(queue) - 1