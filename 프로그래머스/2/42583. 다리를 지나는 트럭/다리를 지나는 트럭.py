from collections import deque
def solution(bridge_length, weight, truck_weights):
    time = 0
    trucks = deque(truck_weights)
    bridge = deque([0] * bridge_length)
    current = 0
    
    while len(trucks) > 0:
        time += 1
        current -= bridge.popleft()
        if current + trucks[0] <= weight:
            current += trucks[0]
            bridge.append(trucks.popleft())
        else:
            bridge.append(0)
            
    time += bridge_length
    
    return time