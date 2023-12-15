n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

ls = a + b
ls.sort()
print(*ls)