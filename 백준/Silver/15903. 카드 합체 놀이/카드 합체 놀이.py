import sys
input = sys.stdin.readline

n, m = map(int, input().split())
cards = list(map(int, input().split()))
cards.sort()

for _ in range(m):
    ans = cards[0] + cards[1]
    cards[0] = ans
    cards[1] = ans
    cards.sort()

print(sum(cards))