import sys
input = sys.stdin.readline


def recur(num):
    if len(ans) == l:
        cnt = 0
        for v in vowels:
            if v in ans:
                cnt += 1
        if 0 < cnt <= l - 2:
            print(''.join(ans))

    for i in range(num, c):
        ans.append(lst[i])
        recur(i + 1)
        ans.pop()


l, c = map(int, input().split())
lst = list(map(str, input().split()))
lst.sort()
vowels = ['a', 'e', 'i', 'o', 'u']
ans = []
recur(0)