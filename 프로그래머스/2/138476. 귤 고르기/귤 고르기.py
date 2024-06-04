from collections import Counter
def solution(k, tangerine):
    t_list = Counter(tangerine)
    sorted_t_list = sorted(t_list.items(), key = lambda item:item[1], reverse = True )

    for i in range(len(sorted_t_list)):
        k -= sorted_t_list[i][1]
        if k <= 0:
            answer = i + 1
            break

    return answer