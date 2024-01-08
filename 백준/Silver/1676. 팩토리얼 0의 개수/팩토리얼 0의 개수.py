n = int(input())
five_count = 0

while n >= 5:
    n //= 5
    five_count += n

print(five_count)