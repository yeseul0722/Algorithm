def solution(n):
    notation = ''
    while n > 0:
        notation += str(n % 3)
        n //= 3
    
    return int(notation, 3)