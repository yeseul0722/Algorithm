import math
def solution(number, limit, power):

    factors = [1]
    for n in range(2, number + 1):
        cnt = 0
        for f in range(1, int(math.sqrt(n)) + 1):
            if n % f == 0:
                cnt += 1
                if f != n // f:
                    cnt += 1
            if cnt > limit:
                cnt = power
                break
        factors.append(cnt)
     
    return sum(factors)