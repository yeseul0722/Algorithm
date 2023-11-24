def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

num1, num2 = map(int, input().split(":"))
gcd_num = gcd(num1, num2)
print(str(int(num1 / gcd_num)) + ":" + str(int(num2 / gcd_num)))
