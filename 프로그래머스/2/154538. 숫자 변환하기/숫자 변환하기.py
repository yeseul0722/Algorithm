from collections import deque
def solution(x, y, n):
    queue = deque([(x, 0)])
    visited = set()
    
    while queue:
        now, cnt = queue.popleft()
        if now == y:
            return cnt
        
        if now + n <= y and not now + n in visited:
            queue.append((now + n, cnt + 1))
            visited.add(now + n)
        if now * 2  <= y and not now * 2 in visited:
            queue.append((now * 2, cnt + 1))
            visited.add(now * 2)
        if now * 3 <= y and not now * 3 in visited:
            queue.append((now * 3, cnt + 1))
            visited.add(now * 3)
        
    return -1