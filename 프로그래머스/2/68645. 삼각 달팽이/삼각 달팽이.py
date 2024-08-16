def solution(n):
    answer = []
    snail = []
    dx = [0, 1, -1]
    dy = [1, 0, -1]
    end_num = 0
    x, y = 0, 0
    dist = 0
    
    for i in range(1, n + 1):
        snail.append([0] * i)
        end_num += i
    
    for num in range(1, end_num + 1):
        snail[y][x] = num
        y += dy[dist]
        x += dx[dist]
        
        if y < 0 or x < 0 or y >= n or x >= len(snail[y]) or snail[y][x] != 0:
            y -= dy[dist]
            x -= dx[dist]
            
            dist = (dist + 1) % 3
            
            y += dy[dist]
            x += dx[dist]
    
    for row in range(n):
        answer += snail[row]
        
    return answer