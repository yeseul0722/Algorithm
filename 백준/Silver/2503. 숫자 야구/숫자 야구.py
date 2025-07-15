import sys
from itertools import permutations

input = sys.stdin.readline
N = int(input())

questions = [list(map(int, input().split())) for _ in range(N)]

count = 0

nums = list(permutations(range(1, 10), 3))

for num in nums:

    valid = True

    for question in questions:
        question_num = list(map(int, str(question[0])))
        answer_strikes, answer_balls = question[1], question[2]

        strikes = balls = 0

        for i in range(3):
            # 같은 자리 같은 숫자
            if num[i] == question_num[i]:
                strikes += 1
            # 다른 자리 같은 숫자
            elif num[i] in question_num:
                balls += 1

        if answer_strikes != strikes or answer_balls != balls:
            valid = False
            break

    if valid:
        count += 1

print(count)
