import sys
input = sys.stdin.readline

arr = list(map(str, input().rstrip()))
arr.sort(reverse = True)
print(int(''.join(arr)))
