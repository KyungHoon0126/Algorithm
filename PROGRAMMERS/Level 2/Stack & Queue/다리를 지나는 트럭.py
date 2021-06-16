
# 스택/큐 - 다리를 지나는 트럭
# 큐를 이용. pop 대신 pop(0)을 사용하면 큐가 된다.

def solution(bridge_length, weight, truck_weights):

    queue = [0] * bridge_length
    sec = 0

    while queue:
        sec += 1
        queue.pop(0)

        if truck_weights:
            if sum(queue) + truck_weights[0] <= weight:
                queue.append(truck_weights.pop(0))
            else:
                queue.append(truck_weights.pop(0))

    return sec