def gcd(a ,b):
    while b > 0:
        a, b = b, a % b
    return a


n = int(input())
for i in range(n):
    data = list(map(int, input().split()))
    data_len = len(data)
    max_gcd = 1
    for j in range(data_len - 1):
        for k in range(j + 1, data_len):
            now_gcd = gcd(data[j], data[k])

            if now_gcd > max_gcd:
                max_gcd = now_gcd

    print(max_gcd)
