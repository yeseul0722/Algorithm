import sys
input = sys.stdin.readline

n = int(input())
ans = n
for _ in range(n):
    word = input()
    alpha = []
    for w in range(len(word)):
        if w >= 1:
            if word[w - 1] != word[w]:
                if word[w] in alpha:
                    ans -= 1
                    break
        alpha.append(word[w])

print(ans)