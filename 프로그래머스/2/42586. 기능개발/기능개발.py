from collections import deque
import math

def solution(progresses, speeds):
    answer = []
    queue = deque([])
    n = len(progresses)
    
    for i in range(n):
        p = math.ceil((100 - progresses[i]) / speeds[i])
        queue.append(p)
        
    while queue:
        cnt = 1
        f = queue.popleft()
        while queue and queue[0] <= f:
            queue.popleft()
            cnt += 1
        answer.append(cnt)
        
    return answer