import sys
from collections import deque

input = sys.stdin.readline

t = int(input())


answer = []
for _ in range(t):
    p = input().strip()
    n = int(input().strip())
    arr = list(input().strip()[1:-1].split(","))
    q = deque(arr)
    reverse = 0
    error = 0
    if n == 0:
        q = []

    for i in p:
        if i == "R":
            reverse = not reverse
        else:
            if len(q) < 1:
                answer.append("error")
                error = 1
                break
            else:
                if reverse:
                    q.pop()
                else:
                    q.popleft()

    if not error:
        if reverse:
            q.reverse()
        answer.append("[" + ",".join(q) + "]")

for a in answer:
    print(a)