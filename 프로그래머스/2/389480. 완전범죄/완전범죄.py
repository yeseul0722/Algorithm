def solution(info, n, m):
    
    dp = [[False] * m for _ in range(n)]
    dp[0][0] = True
    
    for i_a, i_b in info:
        next_dp = [[0] * m for _ in range(n)]
        
        for a in range(n):
            for b in range(m):
                if not dp[a][b]:
                    continue
                    
                if i_a + a < n:
                    next_dp[i_a + a][b] = True
                    
                if i_b + b < m:
                    next_dp[a][i_b + b] = True
                    
        dp = [row[:] for row in next_dp]
                
    for a in range(n):
        for b in range(m):
            if dp[a][b]:
                return a
    
    return -1