def solution(s):
    
    s, N = list(s), len(s)
    if N > 1 and s[0] == s[1]: answer = 2
    else: answer = 1
    
    def lengthPalindrome(start,end):
        length = end - start - 1
        while start >= 0 and end < N and s[start] == s[end]:
            length += 2
            start, end = start-1, end+1
        return length

    for i in range(1,N-1):
        if s[i-1] == s[i+1]:
            answer = max(answer, lengthPalindrome(i-1,i+1))
        if s[i] == s[i+1]:
            answer = max(answer, lengthPalindrome(i,i+1))
    
    return answer
