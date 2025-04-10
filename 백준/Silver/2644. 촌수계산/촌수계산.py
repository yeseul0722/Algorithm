import sys
input = sys.stdin.readline

def dfs(p):
    global cnt
    visited[p] = True

    if p == b:
        print(cnt)
        return

    for i in relationship[p]:
        if not visited[i]:
            cnt += 1
            dfs(i)
            cnt -= 1


n = int(input())
a, b = map(int, input().split())
m = int(input())

relationship = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
cnt = 0

for _ in range(m):
    x, y = map(int, input().split())
    relationship[x].append(y)
    relationship[y].append(x)

dfs(a)
if not visited[b]:
    print(-1)