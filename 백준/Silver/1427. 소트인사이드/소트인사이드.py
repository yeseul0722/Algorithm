import sys
input = sys.stdin.readline

n = input().rstrip()
lst = []
ans = []
for i in n:
    lst.append(int(i))

lst.sort(reverse=True)

for i in lst:
    ans.append(str(i))

print(''.join(ans))