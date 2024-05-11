def solution(numbers, target):
    # 경우의 수 담을 리스트 만들어주기
    lst = [0]

    for i in range(len(numbers)):
        # 이전의 수에 현재 수를 +,- 연산을 수행하며
        # 모든 경우의 수를 임시 리스트에 담아주기
        temp = []
        for j in lst:
            temp.append(j + numbers[i])
            temp.append(j - numbers[i])
        lst = temp
        
        # target과 일치하는 수 반환하기
    return lst.count(target)