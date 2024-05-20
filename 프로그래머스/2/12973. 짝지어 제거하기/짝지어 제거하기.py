def solution(s):
    str_list = list(s) 
    stack = []

    for i in str_list:
        if len(stack) == 0:
            stack.append(i)
        else:
            if stack[-1] == i:
                stack.pop()
            else:
                stack.append(i)

    if len(stack) == 0:
        return 1
    else:
        return 0