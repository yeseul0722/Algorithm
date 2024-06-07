from collections import Counter

def solution(want, number, discount):
    answer = 0
    buy_list = dict(zip(want, number))
    
    for i in range(len(discount) - 9):
        if buy_list == Counter(discount[i : i + 10]):
            answer += 1

            
    return answer