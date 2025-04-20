import sys
input = sys.stdin.readline
N = int(input())
time = []
for _ in range(N):
    start, end = map(int, input().split())
    time.append((start, end))
time.sort(key=lambda x: (x[1], x[0]))
cnt = 1
now = time[0]
for i in range(1, N):
    if time[i][0] >= now[1]:
        now = time[i]
        cnt += 1

print(cnt)