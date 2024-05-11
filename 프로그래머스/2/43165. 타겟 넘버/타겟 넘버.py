def solution(numbers, target):
    lst = [0]
    
    for i in range(len(numbers)):
        temp = []
        for j in lst:
            temp.append(j + numbers[i])
            temp.append(j - numbers[i])
        lst = temp
        
        answer = lst.count(target)
    return answer