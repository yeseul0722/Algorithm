def solution(fees, records):
    car_time = {}
    answer = []
    
    for car in records:
        time, number, status = car.split()
        if not number in car_time:
            car_time[number] = [False, (int(time[:2]) * 60) + (int(time[3:]))]  
        else:
            if status == 'OUT':
                car_time[number][0] = True
                car_time[number][-1] = (int(time[:2]) * 60) + (int(time[3:])) - car_time[number][-1]
            else:
                car_time[number][0] = False
                car_time[number].append((int(time[:2]) * 60) + (int(time[3:])))
    
    sorted_car_time = sorted(car_time.items())
    
    for records in sorted_car_time:
        fee = 0
        total_time = 0
        if records[1][0] == True:
            print(records)
            for record in range(1, len(records[1])):
                total_time += records[1][record]
            total_time -= fees[0]
        else:
            if len(records[1]) >= 3:
                for record in range(1, len(records[1]) - 1):
                    print(record)
                    print(records[1][record])
                    total_time += records[1][record]
            total_time += 1439 - records[1][-1] - fees[0]
        
        if total_time > 0:
            if total_time % fees[2] > 0:
                fee = fees[1] + ((total_time // fees[2]) + 1) * fees[3]
            else:
                fee = fees[1] + (total_time // fees[2]) * fees[3]
            if fee == 0:
                fee = fees[3]
        else:
            fee = fees[1]
                
        answer.append(fee)
    return answer