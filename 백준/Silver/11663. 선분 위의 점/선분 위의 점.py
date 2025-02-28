import sys
input = sys.stdin.readline

def binary_search(v, flag):
    left, right = 0, n - 1
    
    while left <= right:
        mid = (left + right) // 2
        if v < dots[mid]:
            right = mid - 1
        elif v > dots[mid]:
            left = mid + 1
        else:
            return mid
        
    if flag == 0:
        return left
    else:
        return right
        

n, m = map(int, input().split())
dots = list(map(int, input().split()))
dots.sort()

for i in range(m):
    s, e = map(int, input().split())
    l, r = binary_search(s, 0), binary_search(e, 1)
    print(r - l + 1)