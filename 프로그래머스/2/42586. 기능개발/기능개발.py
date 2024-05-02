from collections import deque
def solution(progresses, speeds):
    answer = []
    lst = deque()
    temp = 0
    now = 0
    for i in range(len(progresses)):
        lst.append(progresses[i] + speeds[i])
    while len(lst) >= 0:
        if lst[0] >= 100:
            lst.popleft()
            temp += 1
            if len(lst) == 0:
                answer.append(temp)
                break
            now += 1
        else:
            for i in range(len(lst)):
                lst[i] += speeds[now + i]
            if temp > 0:
                answer.append(temp)
            temp = 0
    return answer
