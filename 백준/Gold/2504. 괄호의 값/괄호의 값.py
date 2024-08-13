import sys
input = sys.stdin.readline

stack = []
s = input().rstrip()
answer = 0
temp = 1

for i in range(len(s)):
    if s[i] == '(':
        stack.append(s[i])
        temp *= 2
    elif s[i] == '[':
        stack.append(s[i])
        temp *= 3
    elif s[i] == ')':
        if not stack or stack[-1] != '(':
            answer = 0
            break
        else:
            if s[i - 1] == '(':
                answer += temp
            stack.pop()
            temp //= 2
    else:
        if not stack or stack[-1] != '[':
            answer = 0
            break
        else:
            if s[i - 1] == '[':
                answer += temp
            stack.pop()
            temp //= 3
if stack:
    print(0)
else:
    print(answer)


