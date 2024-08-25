from itertools import product
def solution(word):
    vowels = ['A', 'E', 'I', 'O', 'U']
    dict = []
    for i in range(1, 6):
        for vowel in product(vowels, repeat = i):
            dict.append(''.join(vowel))
            
    dict.sort()        
    return dict.index(word) + 1