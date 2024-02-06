import sys
input = sys.stdin.readline

n, m = map(int, input().split())
node = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
distance = [[0] * (n + 1) for _ in range(n + 1)]
ans = 0

def dfs(num):
    global ans
    if num == b:
        print(ans)
        return

    for i in node[num]:
        if not visited[i]:
            visited[num] = True
            ans += distance[num][i]
            dfs(i)
            visited[num] = False
            ans -= distance[num][i]


for _ in range(n - 1):
    u, v, d = map(int, input().split())
    node[u].append(v)
    node[v].append(u)
    distance[u][v] = d
    distance[v][u] = d


for _ in range(m):
    a, b = map(int, input().split())
    visited[a] = True
    dfs(a)
    visited[a] = False