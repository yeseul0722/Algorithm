import sys
from collections import deque
input = sys.stdin.readline
queue = deque()

n = int(input())
for _ in range(n):
    data = input().rstrip().split()
    order = data[0]
    if order == 'push':
        queue.append(int(data[1]))
    elif order == 'pop':
        if len(queue) > 0:
            print(queue.popleft())
        else:
            print(-1)
    elif order == 'size':
        print(len(queue))
    elif order == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif order == 'front':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    elif order == 'back':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])