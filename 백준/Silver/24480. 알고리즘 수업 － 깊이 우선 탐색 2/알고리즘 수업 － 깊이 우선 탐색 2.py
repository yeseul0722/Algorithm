import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


def dfs(num):
    global cnt
    visited[num] = cnt
    for i in node[num]:
        if visited[i] == 0:
            cnt += 1
            dfs(i)


n, m, r = map(int, input().split())
node = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)
cnt = 1

for _ in range(m):
    u, v = map(int, input().split())
    node[u].append(v)
    node[v].append(u)

for lst in node:
    lst.sort(reverse=True)

dfs(r)

for row in range(1, n + 1):
    print(visited[row])