from collections import deque

def solution(bridge_length, weight, truck_weights):
    trucks = deque(truck_weights)
    onBridge = deque()
    position = deque()
    
    time = 1
    onBridge.append(trucks.popleft())
    position.append(time)
    while trucks or onBridge:
        time += 1
        if (time - position[0]) == bridge_length:
            onBridge.popleft()
            position.popleft()
        if trucks and sum(onBridge) + trucks[0] <= weight:
            onBridge.append(trucks.popleft())
            position.append(time)
    
    return time
