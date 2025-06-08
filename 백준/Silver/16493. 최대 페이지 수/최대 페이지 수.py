import sys
input = sys.stdin.readline

total_value,total_item = map(int,input().split())

dp = [[0 for _ in range(total_value+1)] for _ in range(total_item+1)]

chapters = []
for _ in range(total_item):
    chapters.append(list(map(int,input().split())))

for i in range(1,total_item+1):
    weight = chapters[i-1][0]
    value = chapters[i-1][1]
    for cur_weight in range(1,total_value+1):
        if weight <= cur_weight:
            dp[i][cur_weight] = max(dp[i-1][cur_weight], dp[i-1][cur_weight-weight]+value)
        else:
            dp[i][cur_weight] = dp[i-1][cur_weight]
print(dp[-1][-1])