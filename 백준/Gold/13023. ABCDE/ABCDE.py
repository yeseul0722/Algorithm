import sys
input = sys.stdin.readline


def dfs(num, depth):
    global flag
    visited[num] = True
    if depth == 5:
        flag = True
        return
    for i in node[num]:
        if not visited[i]:
            dfs(i, depth + 1)
    visited[num] = False


n, m = map(int, input().split())
node = [[] for _ in range(n)]
visited = [False] * n
flag = False

for _ in range(m):
    a, b = map(int, input().split())
    node[a].append(b)
    node[b].append(a)

for i in range(n):
    dfs(i, 1)
    if flag:
        break

if flag:
    print(1)
else:
    print(0)