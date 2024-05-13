from collections import deque
def solution(priorities, location):
    cnt = 0
    queue = deque(priorities)

    while queue:
        location -= 1
        max_num = max(queue)
        temp_num = queue.popleft()
        if temp_num == max_num:
            cnt += 1
        else:
            queue.append(temp_num)
            if location < 0:
                location = len(queue) - 1
        if location < 0:
            break

    return cnt