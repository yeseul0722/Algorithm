import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)


def dfs(num):
    for i in node[num]:
        if not parent[i]:
            parent[i] = num
            dfs(i)

n = int(input())
node = [[] for _ in range(n + 1)]
parent = [0] * (n + 1)


for _ in range(n - 1):
    u, v = map(int, input().split())
    node[u].append(v)
    node[v].append(u)

dfs(1)


for row in parent[2:]:
    print(row)

