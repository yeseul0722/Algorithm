import sys
input = sys.stdin.readline

n = int(input())
calendar = [0]*366

for _ in range(n):
    s, e = map(int, input().split())
    for i in range(s, e+1):
        calendar[i] += 1

row = 0 
col = 0 
result = 0
for day in calendar:
    if day != 0: # 일정이 없는 날이 아닌 경우
        col = max(col, day)
        row += 1
    else: # 일정 없을 때
        result += row * col
        row = 0
        col = 0 # 다시 초기화
result += row * col # 마지막 남은 일정들 더해주기
print(result)