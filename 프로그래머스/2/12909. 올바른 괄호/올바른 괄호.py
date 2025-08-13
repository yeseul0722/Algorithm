from collections import deque

def solution(s):
    stack = deque([])
    
    for i in s:
        if i == '(':
            stack.append(i)
        else:
            if stack:
                stack.popleft()
            else:
                return False
            
    if stack:
        return False
    else:
        return True