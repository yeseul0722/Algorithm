t = int(input())

for _ in range(t):
    stack = []
    data = list(input())
    for i in data:
        if i == "(":
            stack.append(i)
        elif i == ")":
            if stack:
                stack.pop()
            else:
                stack.append(i)
                break
    if len(stack) != 0:
        print("NO")
    else:
        print("YES")