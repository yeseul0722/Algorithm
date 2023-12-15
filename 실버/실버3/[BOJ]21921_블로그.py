import sys
input = sys.stdin.readline

n, x = map(int, input().split())
data = list(map(int, input().split()))

if max(data) == 0:
    print("SAD")
else:
    temp = sum(data[:x])
    max_num = temp
    cnt = 1

    for i in range(x, n):
        temp += data[i]
        temp -= data[i - x]
        if temp > max_num:
            max_num = temp
            cnt = 1
        elif temp == max_num:
            cnt += 1
    print(max_num)
    print(cnt)