import sys
input = sys.stdin.readline


def recur(num):
    global count
    if sum(ans) == s and len(ans) > 0:
        count += 1
    for i in range(num, n):
        ans.append(lst[i])
        recur(i + 1)
        ans.pop()


n, s = map(int, input().split())
lst = list(map(int, input().split()))
ans = []
count = 0

recur(0)
print(count)
