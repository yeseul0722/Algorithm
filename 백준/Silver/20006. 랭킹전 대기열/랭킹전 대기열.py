import sys
input = sys.stdin.readline

p, m = map(int, input().split())
wating = []

for _ in range(p):
    l, n = input().split()
    l = int(l)
    flag = False
    if wating:
        for w in wating:
            if len(w) == m:
                continue
            else:
                if w[0][0] - 10 <= l <= w[0][0] + 10:
                    w.append([l, n])
                    flag = True
                    break

    if not flag:
        wating.append([[l, n]])


for w in wating:
    if len(w) == m:
        print('Started!')
        room = sorted(w, key=lambda x: x[1])
        for r in room:
            print(*r)
    else:
        print('Waiting!')
        room = sorted(w, key=lambda x: x[1])
        for r in room:
            print(*r)

