import sys
input = sys.stdin.readline

n = int(input())
lst = []
for _ in range(n):
    lst.append(int(input()))

lst.sort()
ans = 0

for i in lst:
    ans = max(ans, i * n)
    n -= 1

print(ans)