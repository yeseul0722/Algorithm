import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))
ans = [0] * n
stack = []

for i in range(n):
    while stack:
        if lst[stack[-1][0]] < lst[i]:
            stack.pop()
        else:
            ans[i] = stack[-1][0] + 1
            break
    stack.append([i, lst[i]])

for row in ans:
    print(row, end=' ')