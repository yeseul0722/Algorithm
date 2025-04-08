import sys
input = sys.stdin.readline

n = int(input())
num_lst = list(map(int, input().split()))
num_lst.sort()

if n % 2 == 1:
    print(num_lst[(n - 1) // 2])
else:
    l, r = num_lst[(n - 1) // 2], num_lst[(n - 1) // 2 + 1]
    l_tmp, r_tmp = 0, 0
    for i in range(n):
        l_tmp += abs(num_lst[i] - l)
        r_tmp += abs(num_lst[i] - r)
    if l_tmp >= r_tmp:
        print(l)
    else:
        print(r)

