import sys
input = sys.stdin.readline


def recur(num):
    if len(ans) == m:
        print(*ans)
        return
    for i in range(1, n + 1):
        ans.append(i)
        recur(i)
        ans.pop()


n, m = map(int, input().split())
ans = []
recur(0)