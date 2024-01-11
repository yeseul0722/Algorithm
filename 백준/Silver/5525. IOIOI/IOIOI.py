import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
s = list(input().rstrip())
cnt = 0

for i in range(m):
    if s[i] == 'I':
        temp = 1
        for j in range(i + 1, m):
            if s[j] != s[j - 1]:
                temp += 1
                if temp == n * 2 + 1:
                    cnt += 1
                    break
            else:
                break

print(cnt)