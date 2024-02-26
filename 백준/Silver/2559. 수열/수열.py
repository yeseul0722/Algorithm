import sys
input = sys.stdin.readline

n, k = map(int, input().split())
nums = list(map(int, input().split()))
each = 0

for i in range(k):
    each += nums[i]
maxv = each

for i in range(k, n):
    each += nums[i]
    each -= nums[i - k]
    maxv = max(maxv, each)
    
print(maxv)