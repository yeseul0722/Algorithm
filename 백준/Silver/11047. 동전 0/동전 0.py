import sys
input = sys.stdin.readline

n, k = map(int, input().split())
values = []
ans = 0
for _ in range(n):
    values.append(int(input()))
values.sort(reverse=True)

for i in values:
    if k // i >= 1:
        ans += k // i
        k = k % i
        if k == 0:
            break

print(ans)