import sys
import heapq

def solution(N, road, K):
    answer = 0
    node = [[] for _ in range(N + 1)]
    INF = sys.maxsize
    dist = [INF] * (N + 1)
    for a, b, c in road:
        node[a].append([c, b])
        node[b].append([c, a])
    
    dist[1] = 0
    heap = [[0, 1]]
    
    while heap:
        time, ev = heapq.heappop(heap)
        if dist[ev] != time: continue
        for nt, nv in node[ev]:
            if dist[nv] > time + nt:
                dist[nv] = time + nt
                heapq.heappush(heap, [dist[nv], nv])
                
    for d in dist:
        if d <= K:
            answer += 1
            
    return answer