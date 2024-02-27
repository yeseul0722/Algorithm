import sys
input = sys.stdin.readline

n, d, k, c = map(int, input().split())
lst = []
for _ in range(n):
    lst.append(int(input()))

lp, rp = 0, 0
ans = 0

while lp != n:
    rp = lp + k
    case = set()
    flag = True
    for i in range(lp, rp):
        i %= n
        case.add(lst[i])
        if lst[i] == c:
            flag = False

    cnt = len(case)
    if flag:
        cnt += 1
    ans = max(ans, cnt)
    lp += 1

print(ans)