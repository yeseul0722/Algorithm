from collections import deque

def solution(n, edge):
    answer = 0
    graph = [[]for _ in range(n + 1)]
    distance = [-1] * (n + 1)
    
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)
    
    queue = deque([1])
    distance[1] = 0
    
    while queue:
        now = queue.popleft()
        for i in graph[now]:
            if distance[i] == -1:
                queue.append(i)
                distance[i] = distance[now] + 1
                
    for d in distance:
        if d == max(distance):
            answer += 1

    return answer
