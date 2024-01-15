import sys
sys.setrecursionlimit(150000)
input = sys.stdin.readline


def dfs(num):
    global cnt
    visited[num] = cnt
    node[num].sort()
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

dfs(r)

for num in range(1, n + 1):
    print(visited[num])
