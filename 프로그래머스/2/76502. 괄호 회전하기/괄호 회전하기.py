from collections import deque
def solution(s):
    answer = 0
    queue = deque(s)

    for _ in range(len(s)):
        stack = deque()
        for i in range(len(s)):
            if len(stack) > 0:
                if stack[-1] == '(' and queue[i] == ')':
                    stack.pop()
                elif stack[-1] == '{' and queue[i] == '}':
                    stack.pop()
                elif stack [-1] == '[' and queue[i] == ']':
                    stack.pop()
                else:
                    stack.append(queue[i])
            else:
                stack.append(queue[i])
                
        if len(stack) == 0:
            answer += 1
            
        queue.append(queue.popleft())
        
    return answer