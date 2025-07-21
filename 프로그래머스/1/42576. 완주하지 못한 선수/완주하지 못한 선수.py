from collections import Counter
def solution(participant, completion):
    
    dict = Counter(participant) - Counter(completion)
    return list(dict.keys())[0]