from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    current_weight = 0
    bridge = deque([0] * bridge_length)
    
    while truck_weights:
        answer += 1
        current_weight -= bridge[0]
        bridge.popleft()
        if current_weight + truck_weights[0] <= weight:
            current_weight += truck_weights[0]
            bridge.append(truck_weights.pop(0))
        else:
            bridge.append(0)
    
    return answer + bridge_length