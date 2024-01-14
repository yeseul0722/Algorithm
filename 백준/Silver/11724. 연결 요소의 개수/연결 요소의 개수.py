import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline


def dfs(num):
    if not visited[num]:
        visited[num] = True
        for k in node[num]:
            if not visited[k]:
                    dfs(k)
    visited[num] = True


n, m = map(int, input().split())
node = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)

ans = 0

for _ in range(m):
    u, v = map(int, input().split())
    node[u].append(v)
    node[v].append(u)

for i in range(1, n + 1):
    if not visited[i]:
        dfs(i)
        ans += 1

print(ans)