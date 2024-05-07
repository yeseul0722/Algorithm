def solution(s):
    answer = []
    lst = s.split(' ')

    for i in lst:
        word = ''
        for j in range(len(i)):
            if j == 0:
                word += i[j].upper()
            else:
                word += i[j].lower()
        answer.append(word)
    
    answer = ' '.join(answer)
            
    return answer