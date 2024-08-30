from collections import deque
def solution(dirs):
    answer = 0
    dir = {'U': (1, 0), 'D': (-1, 0), 'R': (0, 1), 'L': (0, -1)}
    road = deque()
    y, x = 0, 0
    
    for i in dirs:
        ny, nx = y + dir[i][0], x + dir[i][1]
        if -5 <= ny <= 5 and -5 <= nx <= 5:
            if not [(y, x), (ny, nx)] in road:
                road.append([(y, x), (ny, nx)])
                road.append([(ny, nx), (y, x)])
            y, x = ny, nx
            
    return len(road) // 2