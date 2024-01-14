import sys
input = sys.stdin.readline


def dfs(num):
    if not visited[num]:
        visited[num] = True
        for k in board[num]:
            a.add(num)
            b.add(k)

            if a == b:
                ans.extend(list(b))
                return
            dfs(k)
    visited[num] = False


n = int(input())
board = [[] for _ in range(n + 1)]

# for i in range(1, n + 1):
#     board[i].append(i)

for i in range(1, n + 1):
    board[i].append(int(input()))
ans = []

for i in range(1, n + 1):
    visited = [False] * (n + 1)
    a = set()
    b = set()

    dfs(i)

ans = list(set(ans))
ans.sort()

print(len(ans))
for j in ans:
    print(j)
