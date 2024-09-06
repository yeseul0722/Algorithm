from itertools import product
def solution(word):
    answer = 0
    vowels = ['A', 'E', 'I', 'O', 'U']
    dict = []
    
    for i in range(1, 6):
        for p in product(vowels, repeat = i):
            dict.append(''.join(p))
    dict.sort()
    
    return dict.index(word) + 1