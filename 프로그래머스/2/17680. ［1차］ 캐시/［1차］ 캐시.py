from collections import deque
def solution(cacheSize, cities):
    answer = 0
    queue = deque()
    
    for city in cities:
        city = city.lower()
        if cacheSize:
            if not city in queue:
                if cacheSize == len(queue):
                    queue.popleft()
                queue.append(city)
                answer += 5
            else:
                queue.remove(city)
                queue.append(city)
                answer += 1
        else:
            answer += 5
                
    return answer