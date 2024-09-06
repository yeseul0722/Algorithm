import heapq, sys
def solution(N, road, K):
    INF = sys.maxsize
    node = [[] for _ in range(N + 1)]
    dist = [INF] * (N + 1)
    heap = [[0, 1]]
    dist[1] = 0
    
    for a, b, c in road:
        node[a].append([c, b])
        node[b].append([c, a])
        
    while heap:
        ew, ev = heapq.heappop(heap)
        if ew != dist[ev]:
            continue
        for nw, nv in node[ev]:
            if dist[nv] > ew + nw:
                dist[nv] = ew + nw
                heapq.heappush(heap, [dist[nv], nv])
    answer = 0                
    for i in range(1, N + 1):
        if dist[i] <= K:
            answer += 1
            
    return answer