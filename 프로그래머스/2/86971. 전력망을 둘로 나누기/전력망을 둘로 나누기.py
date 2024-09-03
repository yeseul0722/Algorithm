from collections import deque
def solution(n, wires):
    answer = 101
    node = [[] for _ in range(n + 1)]
    
    def bfs(start):
        queue = deque([start])
        visited = [False] * (n + 1)
        cnt = 0
        
        while queue:
            now = queue.popleft()
            visited[now] = True
            cnt += 1
            
            for i in node[now]:
                if not visited[i]:
                    queue.append(i)
                    
        return cnt 
    
    for a, b in wires:
        node[a].append(b)
        node[b].append(a)
        
    for a, b in wires:
        node[a].remove(b)
        node[b].remove(a)
        
        cnt = bfs(a)
        answer = min(answer, abs((n - cnt) - cnt))
        
        node[a].append(b)
        node[b].append(a)
        
    return answer