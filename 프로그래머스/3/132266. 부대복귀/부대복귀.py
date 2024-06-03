from collections import deque
def solution(n, roads, sources, destination):
    graph = [[] for _ in range(n + 1)]
    visited = [-1] * (n + 1)
    visited[destination] = 0

    for x, y in roads:
        graph[x].append(y)
        graph[y].append(x)

    visited = bfs(destination, graph, visited)

    return [visited[i] for i in sources]

def bfs(destination, graph, visited):
    queue = deque([destination])

    while queue:
        now = queue.popleft()
        for next in graph[now]:
            if visited[next] == -1:
                visited[next] = visited[now] + 1
                queue.append(next)

    return visited