import sys

sys.setrecursionlimit(100000000)

N, M, R = map(int, sys.stdin.readline().split())

graph = [[] for i in range(N + 1)]
visited = [0 for i in range(N + 1)]
visited[R] = 1
cnt = 1

for i in range(M):
    s, e = map(int, sys.stdin.readline().split())

    graph[s].append(e)
    graph[e].append(s)

for i in range(N + 1):
    graph[i].sort(reverse = True)

def DFS(n):
    global cnt

    for nxt in graph[n]:
        if visited[nxt] != 0:
            continue

        cnt += 1
        visited[nxt] = cnt
        DFS(nxt)

DFS(R)

for i in range(1, N + 1):
    print(visited[i])