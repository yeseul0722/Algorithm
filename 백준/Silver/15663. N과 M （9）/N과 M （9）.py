import sys
input = sys.stdin.readline

def recur(num):
    if len(ans) == m:
        print(*ans)
        return
    remember = 0
    for i in range(len(lst)):
        if not chk[i] and remember != lst[i]:
            chk[i] = True
            ans.append(lst[i])
            remember = lst[i]
            recur(i + 1)
            ans.pop()
            chk[i] = False


n, m = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
ans = []
chk = [False] * n

recur(0)