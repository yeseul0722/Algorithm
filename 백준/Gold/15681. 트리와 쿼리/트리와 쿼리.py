import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(num):
    visited[num] = True
    for i in node[num]:
        if not visited[i]:
            dfs(i)
            count[num] += count[i]

n, r, q = map(int, input().split())
node = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
count = [1] * (n + 1)

for _ in range(n - 1):
    u, v = map(int, input().split())
    node[u].append(v)
    node[v].append(u)

dfs(r)

for _ in range(q):
    u = int(input())
    print(count[u])
