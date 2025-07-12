import sys

n = int(input())
nums = []

for _ in range(n):
    nums.append(int(sys.stdin.readline()))

nums.sort()

for num in nums:
    print(num)