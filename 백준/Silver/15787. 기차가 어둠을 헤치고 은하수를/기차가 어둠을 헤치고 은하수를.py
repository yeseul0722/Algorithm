tc, oc = map(int, input().split())              # tc 기차의 수 oc 명령의 수

trains = [['0']*20 for _ in range(tc)]

for num in range(oc):
    order = list(map(int, input().split()))     # 명령

    if order[0] ==  1:                          # i번째 기차 x번째 좌석에 사람 태워라
        trains[order[1]-1][order[2]-1] = '1'
    
    elif order[0] == 2:                         # i번째 기차 x번째 좌석에 앉은 사람 하차
        trains[order[1]-1][order[2]-1] = '0'
    
    elif order[0] == 3:                         # i번째 기차에 앉은 승객 모두 한칸씩 뒤로
        trains[order[1]-1].insert(0, '0')
        trains[order[1]-1].pop(20)
    
    elif order[0] == 4:                         # i번째 기차에 앉은 승객 모두 한칸씩 앞으로
        trains[order[1]-1].insert(20, '0')
        trains[order[1]-1].pop(0)

answers = set()

for train in trains:
    answers.add("".join(train))

print(len(answers))