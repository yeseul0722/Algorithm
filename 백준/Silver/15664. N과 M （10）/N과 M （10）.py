import sys
input = sys.stdin.readline


def recur(num):
    if len(ans) == m:
        print(' '.join(map(str,ans)))
        return
    remember = 0
    for i in range(num ,n):
        if not visited[i] and remember != lst[i]:
            visited[i] = True
            ans.append(lst[i])
            remember = lst[i]
            recur(i + 1)
            visited[i] = False
            ans.pop()


n, m = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
visited = [False] * n
ans = []

recur(0)