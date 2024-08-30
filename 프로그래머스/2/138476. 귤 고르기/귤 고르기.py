from collections import Counter
def solution(k, tangerine):

    dic = Counter(tangerine)
    size = []
    for key, value in dic.items():
        size.append(value)
    size.sort(reverse = True)
    
    for i in range(len(size)):
        k -= size[i]
        if k <= 0:
            return i + 1