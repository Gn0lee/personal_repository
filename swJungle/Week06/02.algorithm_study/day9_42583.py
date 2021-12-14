def solution(bridge_length, weight, truck_weights):
    from collections import deque
    
    answer = 0
    truck_weights = deque(truck_weights)
    
    num_trucks = len(truck_weights)
    on_bridge = deque([])
    finish_trucks = []
    time = deque([])

    while len(finish_trucks) < num_trucks:
    
        if on_bridge and  time[0] == bridge_length:
            finish_trucks.append(on_bridge.popleft())
            time.popleft()
        if truck_weights and on_bridge and sum(on_bridge) + truck_weights[0] <= weight:
            on_bridge.append(truck_weights.popleft())
            time.append(0)
        if not on_bridge and truck_weights:
            on_bridge.append(truck_weights.popleft())
            time.append(0)
        
        for i in range(len(time)):
             time[i] += 1
        
        answer += 1
        
    return answer


print(solution(2,10,[7,4,5,6]))
