import sys
input = sys.stdin.readline

n = int(input())
distances = list(map(int, input().split()))
prices = list(map(int, input().split()))

answer = distances[0] * prices[0]
min_price = prices[0]

for i in range(1, n - 1):
    if min_price > prices[i]:
        min_price = prices[i]
    answer += distances[i] * min_price

print(answer)