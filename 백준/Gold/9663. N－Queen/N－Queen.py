import sys
input = sys.stdin.readline

n = int(input())


def dfs(num):
    global ans
    if num == n:
        ans += 1
        return

    for j in range(n):
        if v1[j] == v2[num + j] == v3[num - j] == 0: # 열/대각선 퀸 없는 경우
            v1[j] = v2[num + j] = v3[num - j] = 1
            dfs(num + 1)
            v1[j] = v2[num + j] = v3[num - j] = 0


ans = 0
v1 = [0] * n
v2 = [0] * (2 * n)
v3 = [0] * (2 * n)
dfs(0)
print(ans)