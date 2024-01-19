import sys
input = sys.stdin.readline


def recur(num):
    if len(ans) == m:
        print(*ans)
        return
    for i in range(num, n):
        ans.append(lst[i])
        recur(i + 1)
        ans.pop()


n, m = map(int, input().split())
lst = list(map(int, input().split()))
ans = []
lst.sort()

recur(0)
