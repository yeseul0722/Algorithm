import sys
input = sys.stdin.readline

n, k = map(int, input().split())
temp = 0
sieve = [True] * (n + 1)
for i in range(2, n + 1):
    for j in range(i, n + 1, i):
        if sieve[j]:
            sieve[j] = False
            temp += 1
            if temp == k:
                print(j)
                