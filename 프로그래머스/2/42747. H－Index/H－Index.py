def solution(citations):
    answer = 0
    citations.sort(reverse = True)
    
    for i in range(len(citations)):
        if i + 1 <= citations[i]:
            answer = i + 1
            
    return answer