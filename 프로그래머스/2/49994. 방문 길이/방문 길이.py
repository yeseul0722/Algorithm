def solution(dirs):
    dir = {'U': (1, 0), 'D': (-1, 0), 'R': (0, 1), 'L': (0, -1)}
    answer = []
    
    y, x = 0, 0
    for d in dirs:
        ny = y + dir[d][0]
        nx = x + dir[d][1]
        if -5 <= ny <= 5 and -5 <= nx <= 5:
            if not [(y, x), (ny, nx)] in answer:
                answer.append([(y, x), (ny, nx)])
                answer.append([(ny, nx), (y, x)])
            y, x = ny, nx
            
    return len(answer) // 2