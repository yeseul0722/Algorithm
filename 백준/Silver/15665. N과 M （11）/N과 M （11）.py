import sys
input = sys.stdin.readline

def recur(num):
    if len(ans) == m:
        print(' '.join(map(str, ans)))
        return
    remember = 0
    for i in range(n):
        if remember != lst[i]:
            remember = lst[i]
            ans.append(lst[i])
            recur(i + 1)
            ans.pop()


n, m = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
ans = []
recur(0)