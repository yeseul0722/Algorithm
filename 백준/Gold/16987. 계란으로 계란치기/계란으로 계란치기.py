import sys
input = sys.stdin.readline


def recur(num):
    global answer
    if num == n:
        cnt = 0
        for i in range(n):
            if eggs[i][0] <= 0:
                cnt += 1
        answer = max(cnt, answer)
        return
    if eggs[num][0] <= 0:
        recur(num + 1)
        return
    check = True
    for i in range(n):
        if i == num:
            continue
        if eggs[i][0] > 0:
            check = False
            break
    if check:
        answer = max(answer, n -1)
        return
    for i in range(n):
        if i == num:
            continue
        if eggs[i][0] <= 0:
            continue
        eggs[num][0] -= eggs[i][1]
        eggs[i][0] -= eggs[num][1]
        recur(num + 1)
        eggs[num][0] += eggs[i][1]
        eggs[i][0] += eggs[num][1]


n = int(input())
eggs = []
for _ in range(n):
    s, w = map(int, input().split())
    eggs.append([s, w])
answer = 0

recur(0)
print(answer)