def solution(citations):
    answer = 0
    citations.sort(reverse=True)

    for num, citation in enumerate(citations):
        if citation >= num + 1:
            answer = num + 1

    return answer

