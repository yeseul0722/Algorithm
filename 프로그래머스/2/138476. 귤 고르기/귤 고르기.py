from collections import Counter
def solution(k, tangerine):

    n = len(tangerine)
    dic = Counter(tangerine)
    size = []
    for key, value in dic.items():
        size.append(value)
    size.sort()
    for i in range(len(size)):
        n -= size[i]
        if n == k:
            return len(size[i + 1:])
        if n < k:
            return len(size[i:])