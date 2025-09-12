def solution(numbers, target):
    lst = [0]
    
    for i in range(len(numbers)):
        tmp = []
        for j in lst:
            tmp.append(j + numbers[i])
            tmp.append(j - numbers[i])
        lst = tmp
    return lst.count(target)