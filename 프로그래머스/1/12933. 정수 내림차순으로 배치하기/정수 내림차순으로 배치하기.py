def solution(n):
    s = list(str(n))
    s.sort(reverse = True)
    return int(''.join(s))