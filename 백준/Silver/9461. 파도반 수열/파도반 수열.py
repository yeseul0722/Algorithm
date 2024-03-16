import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    if n < 3:
        print(1)
        continue

    dp = [0] * n
    for i in range(3):
        dp[i] = 1
    for i in range(3, n):
        dp[i] = dp[i - 3] + dp[i - 2]

    print(dp[n - 1])
