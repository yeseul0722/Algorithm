import math

def solution(n, words):
    answer = [0, 0]
    save_words = {}
    save_words[words[0]] = 1
    
    for i in range(1, len(words)):
        if words[i - 1][-1] != words[i][0] or words[i] in save_words:
            answer[0] = i % n + 1
            answer[1] = math.ceil((i + 1) / n)
            break
        save_words[words[i]] = 1

    return answer