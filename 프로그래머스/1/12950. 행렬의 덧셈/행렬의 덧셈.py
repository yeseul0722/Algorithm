def solution(arr1, arr2):
    answer = [[0] * len(arr1[0]) for _ in range(len(arr1))]
    for y in range(len(arr1)):
        for x in range(len(arr1[0])):
            answer[y][x] = arr1[y][x] + arr2[y][x]
    return answer