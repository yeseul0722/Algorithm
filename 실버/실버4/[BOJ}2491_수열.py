N = int(input())
numbers = list(map(int, input().split()))
max_increase = 1
max_decrease = 1

increase = 1
decrease = 1

for i in range(1, N):
    if numbers[i - 1] <= numbers[i]:
        increase += 1
        if increase > max_increase:
            max_increase = increase
    else:
        increase = 1

for i in range(1, N):
    if numbers[i - 1] >= numbers[i]:
        decrease += 1
        if decrease > max_decrease:
            max_decrease = decrease
    else:
        decrease = 1

print(max(max_increase, max_decrease))