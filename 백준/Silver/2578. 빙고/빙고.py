import sys
input = sys.stdin.readline

board = []
nums = []
ans = 0
tmp = 0

def bingo():
    cnt = 0
    for i in range(5):
        if board[i] == [0] * 5:
            cnt += 1

    for i in range(5):
        if all(board[j][i] == 0 for j in range(5)):
            cnt += 1

    if all(board[i][i] == 0 for i in range(5)):
        cnt += 1
    if all(board[i][4 - i] == 0 for i in range(5)):
        cnt += 1
    return cnt


for _ in range(5):
    board.append(list(map(int, input().split())))
for _ in range(5):
    nums += list(map(int, input().split()))

for n in range(25):
    for y in range(5):
        for x in range(5):
            if nums[n] == board[y][x]:
                board[y][x] = 0
                tmp += 1
                break

    if tmp >= 12:
        ans = bingo()
        if ans >= 3:
            print(n + 1)
            break
