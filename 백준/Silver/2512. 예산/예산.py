import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))
m = int(input())
start, end = 0, max(lst)

while start <= end:
    mid = (start + end) // 2
    sum = 0
    for i in lst:
        if i <= mid:
            sum += i
        else:
            sum += mid

    if sum <= m:
        start = mid + 1
    else:
        end = mid - 1

print(end)