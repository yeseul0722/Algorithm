import sys
input = sys.stdin.readline

words = []
n = int(input())
for i in range(n):
    words.append(input().rstrip())

words = list(set(words))
words.sort()
words.sort(key=len)

for j in words:
    print(j)