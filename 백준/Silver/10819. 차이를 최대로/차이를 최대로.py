import sys
input = sys.stdin.readline


def dfs():
    global ans
    if len(check) == n:
        temp = 0
        for a in range(1, n):
            temp += abs(check[a - 1] - check[a])
        if temp > ans:
            ans = temp
        return

    for i in range(n):
        if not visited[i]:
            visited[i] = True
            check.append(lst[i])
            dfs()
            check.pop()
            visited[i] = False


n = int(input())
lst = list(map(int, input().split()))
visited = [False] * n
check = []
ans = 0

dfs()
print(ans)
