from itertools import product
def solution(word):
    dict = []
    vowels = ['A', 'E', 'I', 'O', 'U']
    for i in range(1, 6):
        for v in product(vowels, repeat = i):
            dict.append(''.join(list(v)))
    dict.sort()
    return dict.index(word) + 1