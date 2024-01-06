import sys
input = sys.stdin.readline


count = 1
temp = True
stack = []
ans = []

n = int(input())
for _ in range(n):
    num = int(input())
    while count <= num:
        stack.append(count)
        ans.append('+')
        count += 1
    if stack[-1] == num:
        stack.pop()
        ans.append('-')
    else:
        temp = False
        break

if temp == False:
    print('NO')
else:
    for i in ans:
        print(i)