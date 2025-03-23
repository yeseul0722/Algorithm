import sys
input = sys.stdin.readline
N = int(input())
blocks = list(input().rstrip())
visited = True
dp = list([1e9, not visited] for _ in range(N))
dp[0][0], dp[0][1] = 0, True


for i in range(1, N):
    block = blocks[i]
    check_jump = '?'

    if block == 'B':
        check_jump = 'J'
    elif block == 'O':
        check_jump = 'B'
    else:
        check_jump = 'O'

    for j in range(i):
        if check_jump == blocks[j]:
            # j -> i로 점프
            dp[i][0] = min(dp[i][0], dp[j][0] + pow(i-j, 2))

            if dp[i][0] != 1e9:
                dp[i][1] = True

if dp[N-1][1]:
    print(dp[N-1][0])
else:
    print(-1)