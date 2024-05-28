from collections import deque
def solution(skill, skill_trees):
    answer = 0

    for skill_tree in skill_trees:
        queue = deque(skill)
        flag = True

        for char in skill_tree:
            if not char in queue:
                continue
            else:
                if char == queue[0]:
                    queue.popleft()
                else:
                    flag = False
                    break
        if flag:
            answer += 1

    return answer