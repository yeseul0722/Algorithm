import sys
from collections import deque
input = sys.stdin.readline


def recur(l, num):
    global ans
    val = 0
    if l == m:
        for h in house:
            hr, hc = h[0], h[1]
            dist = 2 * n

            for c in select:
                cr, cc = c[0], c[1]
                temp = abs(hr - cr) + abs(hc - cc)
                if temp < dist:
                    dist = temp
            val += dist

        if val < ans:
            ans = min(val, ans)
            return

    for i in range(num, k):
        select.append(chicken[i])
        recur(l + 1, i + 1)
        select.pop()



n, m = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

chicken = deque()
house = deque()

select = deque([])
for y in range(n):
    for x in range(n):
        if board[y][x] == 1:
            house.append((y, x))
        elif board[y][x] == 2:
            chicken.append((y, x))


k = len(chicken)
ans = n * 2 * len(house)

for t in range(k):
    recur(0, t)

print(ans)