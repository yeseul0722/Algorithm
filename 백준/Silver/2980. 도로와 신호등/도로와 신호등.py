import sys
input = sys.stdin.readline

n, l = map(int, input().split())
ans = 0
now = 0

for _ in range(n):
    d, r, g = map(int, input().split())

    ans += (d - now)
    now = d
    if ans % (r + g) <= r:
        ans += (r - (ans % (r + g)))

ans += (l - now)
print(ans)


