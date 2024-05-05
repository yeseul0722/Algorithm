def solution(A,B):
    answer = 0
    A.sort()
    B.sort()
    
    for _ in range(len(A)):
        minA = A[0]
        minB = B[0]
        
        if minA <= minB:
            answer += minA * B[-1]
            A.pop(0)
            B.pop()
        else:
            answer += minB * A[-1]
            B.pop(0)
            A.pop()
    
    return answer