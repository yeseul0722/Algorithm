def solution(brown, yellow):
    
    for i in range(1, int(yellow ** (1/2)) + 1):
        if yellow % i == 0 and ((i + 1) * 2) + ((yellow // i + 1) * 2) == brown:
            return [(yellow // i) + 2, i + 2]