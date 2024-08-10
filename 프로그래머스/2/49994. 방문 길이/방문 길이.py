def solution(dirs):
    visited = set()
    direction =  {'U': (1, 0), 'D': (-1, 0), 'R': (0, 1), 'L': (0, -1)}
    y, x = 0, 0
    
    for d in dirs:
        dy, dx = direction[d]
        ny, nx = y + dy, x + dx
        if -5 <= ny < 6 and -5 <= nx < 6:
            visited.add(((y, x), (ny, nx)))
            visited.add(((ny, nx), (y, x)))
            y, x = ny, nx
            
    return len(visited) // 2