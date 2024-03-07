import sys
input = sys.stdin.readline

n = int(input())
lst = [int(input()) for _ in range(n)]
ans = 0

for i in range(n - 2, -1, -1):
    if lst[i] >= lst[i + 1]:
        ans += (lst[i] - lst[i + 1]) + 1
        lst[i] = lst[i + 1] - 1

print(ans)