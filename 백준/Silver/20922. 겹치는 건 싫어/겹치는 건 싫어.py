import sys
input = sys.stdin.readline

n, k = map(int, input().split())
lst = list(map(int, input().split()))
check = [0] * (max(lst) + 1)

lp, rp = 0, 0
ans = 0

while rp < n:
    if check[lst[rp]] < k:
        check[lst[rp]] += 1
        rp += 1
    else:
        check[lst[lp]] -= 1
        lp += 1
    ans = max(ans, rp - lp)

print(ans)
