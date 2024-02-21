import sys
input = sys.stdin.readline

n = int(input())
books = {}

for _ in range(n):
    book = input().rstrip()
    if not book in books:
        books[book] = 1
    else:
        books[book] += 1

max_book = max(books.values())

best = []
for key, value in books.items():
    if value == max_book:
        best.append(key)

best.sort()
print(best[0])