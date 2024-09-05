import sys
input = sys.stdin.readline

n = int(input())
num = 666

while True:
    if '666' in str(num):
        n -= 1
    if n == 0:
        break

    num += 1
print(num)
