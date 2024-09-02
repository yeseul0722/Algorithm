from collections import deque
def solution(people, limit):
    answer = 0
    people.sort(reverse = True)
    queue = deque(people)
    
    while queue:
        weight = queue.popleft()
        if queue and queue[-1] + weight <= limit:
            weight += queue.pop()
        answer += 1
        
    return answer