def solution(s):
    answer = []
    dict = {}
    for i in range(len(s)):
        if not s[i] in dict:
            answer.append(-1)
        else:
            answer.append(i - dict[s[i]])
        dict[s[i]] = i
    return answer