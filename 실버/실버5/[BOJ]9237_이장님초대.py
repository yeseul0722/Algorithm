n = int(input())
data = list(map(int, input().split()))
data.sort(reverse=True)
day = n + 1

max = 0
for i in range(1, n + 1):
    N = data[i-1] + i
    if N > max:
        max = N

print(max + 1)