import sys
input = sys.stdin.readline


def recur(num):
    if len(ans) == m:
        print(*ans)
        return
    for i in range(num, n):
            ans.append(lst[i])
            recur(i)
            ans.pop()


n, m = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
ans = []

recur(0)