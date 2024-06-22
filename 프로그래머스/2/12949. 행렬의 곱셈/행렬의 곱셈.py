def solution(arr1, arr2):
    n = len(arr1)
    m = len(arr2[0])
    answer = [[0] * m for _ in range(n)]
    
    for y in range(n):
        for x in range(m):
            for z in range(len(arr1[0])):
                answer[y][x] += arr1[y][z] * arr2[z][x]
            
    return answer