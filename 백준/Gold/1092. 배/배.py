import sys
input = sys.stdin.readline

n = int(input())
cranes = list(map(int, input().split()))
m = int(input())
boxes = list(map(int, input().split()))

cranes.sort(reverse=True)
boxes.sort(reverse=True)

cnt = 0

if cranes[0] < boxes[0]:cnt = -1
else:
    while boxes:
        for c in cranes:
            if boxes and c < boxes[-1]:
                continue
            for b in boxes:
                if b <= c:
                    boxes.remove(b)
                    break
        cnt += 1

print(cnt)