import sys
input = sys.stdin.readline

n = int(input())
lst = []
for _ in range(n):
    lst.append(int(input()))

lst.sort()
ans = []

for i in lst:
    ans.append(i * n)
    n -= 1

print(max(ans))