def solution(clothes):
    answer = 1
    hash = {}

    # 같은 의상들끼리 묶어주기
    for lst in clothes:
        if lst[1] in hash:
            hash[lst[1]] += 1
        else:
            hash[lst[1]] = 1

    # 의상 입을 수 있는 경우의 수 + 1(입지 않을 경우의 수)
    for i in hash:
        answer *= hash[i] + 1

    # 모두 안입은 경우 빼주기
    answer -= 1
    return answer

