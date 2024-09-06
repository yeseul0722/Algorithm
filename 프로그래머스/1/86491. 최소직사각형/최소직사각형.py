def solution(sizes):
    w, h = 0, 0
    for i in range(len(sizes)):
        sizes[i].sort()
        w = max(w, sizes[i][0])
        h = max(h, sizes[i][1])
    
    return w * h