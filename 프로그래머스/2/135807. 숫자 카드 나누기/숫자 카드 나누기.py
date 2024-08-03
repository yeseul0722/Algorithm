def solution(arrayA, arrayB):
    answer = 0
    
    gcdA = arrayA[0]
    gcdB = arrayB[0]
    
    for i in arrayA[1:]:
        gcdA = gcd(i, gcdA)
        
    for j in arrayB[1:]:
        gcdB = gcd(j, gcdB)
        
    if notDiv(arrayA, gcdB):
        answer = max(answer, gcdB)
    
    if notDiv(arrayB, gcdA):
        answer = max(answer, gcdA)
        
    return answer


def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)
    
def notDiv(array, gcd):
    for n in array:
        if n % gcd == 0:
            return False
    return True