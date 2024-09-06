import copy
from collections import deque
def solution(s):
    answer = 0
    s = deque(list(s))
    
    for _ in range(len(s)):
        s.append(s.popleft())
        tmp = copy.deepcopy(s)
        stack = []
        
        while tmp:
            char = tmp.popleft()
            if char == '(' or char == '[' or char == '{':
                stack.append(char)
            elif char == ')':
                if stack and stack[-1] == '(':
                    stack.pop()
                else:
                    stack.append(char)
                    break
            elif char == ']':
                if stack and stack[-1] == '[':
                    stack.pop()
                else:
                    stack.append(char)
                    break
            else:
                if stack and stack[-1] == '{':
                    stack.pop()
                else:
                    stack.append(char)
                    break
                    
        if not stack:
            answer += 1
    return answer