import sys
from collections import deque
input = sys.stdin.readline

n, w, l = map(int, input().split())
trucks = deque(list(list(map(int, input().split()))))
bridge = deque([0] * w)
time = 0

while bridge:
    time += 1
    bridge.popleft()
    if trucks:
        if sum(bridge) + trucks[0] <= l:
            bridge.append(trucks.popleft())
        else:
            bridge.append(0)

print(time)




