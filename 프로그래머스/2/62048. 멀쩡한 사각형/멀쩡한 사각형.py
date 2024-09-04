import math
def solution(w,h):
    k = math.gcd(w, h)
    return w * h - (w + h - k)