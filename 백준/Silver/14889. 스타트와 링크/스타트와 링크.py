import sys
input = sys.stdin.readline


def recur(l, num):
    global ans
    if l == n//2:
        a = 0
        b = 0
        for y in range(n):
            for x in range(n):
                if visited[y] and visited[x]:
                    a += board[y][x]
                elif not visited[y] and not visited[x]:
                    b += board[y][x]
        ans = min(ans, abs(a - b))
        return
    for i in range(num, n):
        if not visited[i]:
            visited[i] = True
            recur(l + 1, i + 1)
            visited[i] = False


n = int(input())
board = []
visited = [False for _ in range(n)]

for _ in range(n):
    data = list(map(int, input().split()))
    board.append(data)

ans = 101
recur(0, 0)
print(ans)