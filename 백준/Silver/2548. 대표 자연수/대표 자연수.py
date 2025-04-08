import sys
input = sys.stdin.readline

n = int(input())
num_lst = list(map(int, input().split()))
num_lst.sort()

print(num_lst[(n - 1) // 2])
