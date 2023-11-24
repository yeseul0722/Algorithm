K = int(input())

for i in range(1, K + 1):
    inputs = list(map(int, input().split()))
    N = inputs[0]
    grades = inputs[1:]
    grades.sort(reverse=True)
    max_num = max(grades)
    min_num = min(grades)
    max_gap = 0
    for j in range(N - 1):
        gap = grades[j] - grades[j + 1]
        if gap > max_gap:
            max_gap = gap
    print('Class', i)
    print('Max', max_num,end=', ')
    print('Min', min_num,end=', ')
    print('Largest gap', max_gap)