import copy
from collections import deque
def solution(s):
    answer = 0
    queue = deque(s)

    for _ in range(len(s)):
        string = queue.popleft()
        queue.append(string)
        copy_q = copy.deepcopy(queue)
        stack = deque()
        stack.append(copy_q.popleft())
        
        while copy_q:
            temp = copy_q.popleft()
            if temp == '(' or temp == '[' or temp == '{':
                stack.append(temp)
            elif temp == ')':
                if len(stack) == 0 or not stack[-1] == '(':
                    stack.append(temp)
                    break
                else:
                    stack.pop()
            elif temp == '}':
                if len(stack) == 0 or not stack[-1] == '{':
                    stack.append(temp)
                    break
                else:
                    stack.pop()
            elif temp == ']':
                if len(stack) == 0 or not stack[-1] == '[':
                    stack.append(temp)
                    break
                else:
                    stack.pop()
        if len(stack) == 0:
            answer += 1

    return answer