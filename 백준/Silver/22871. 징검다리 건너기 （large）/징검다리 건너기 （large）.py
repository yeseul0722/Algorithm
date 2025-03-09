import sys
input = sys.stdin.readline
 
n = int(input())
stones = list(map(int, input().split()))
 
def power(i, j):
    return (i - j)*(1 + abs(stones[i]-stones[j]))
 
dp = [int(1e9)] * n
dp[0] = 0
for i in range(1, n):
    for j in range(i):
        # j번째 돌을 밟고 i번째 돌로 가기
        dp[i] = min(max(dp[j], power(i, j)), dp[i])
print(dp[n-1])
