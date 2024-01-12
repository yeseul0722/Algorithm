import sys
input = sys.stdin.readline

word = input().rstrip()
length = len(word)
s = []
for i in range(length):
    s.append(word[i])
    for j in range(i + 1, length):
        s.append(word[i : j + 1])


print(len(set(s)))