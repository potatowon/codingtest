'''
commit : 0302 스택:다리를 지나는 트럭

bridge_length = 다리에 올라갈 수 있는 최대의 트럭수(다리의 길이)
weight = 최대 하중(단, 완전히 오르지 않은 트럭은 무시)

while True:
    시간 += 1
    if truck_weight:
        시작 트럭 = truck_weight.popleft()
        if 다리 하중 > 현재 다리 하중 + 시작트럭 무게:
            다리위.append(시작트럭)
            현재 무게 += 현재 트럭
        else:
            다리위 .append(0)
            트럭.appendleft(현재 트럭)
        if 다리길이 = 다리 위 길이:
            현재 다리 무게 -= 다리위 길이.popleft()
    else:
        if 다리 길이 > 다리 위 길이:
            다리위.append(0)
        elif 다리길이 == 다리 위 길이:
            return answer

'''
from collections import deque

def solution(bridge_length, weight, truck_weights):
    on_bridge = deque()
    truck_weights =deque(truck_weights)
    bridge_weight = 0
    answer = 0
    while True:
        answer += 1
        if truck_weights:
            start_truck = truck_weights.popleft()
            if weight >= bridge_weight + start_truck:
                on_bridge.append(start_truck)
                bridge_weight += start_truck
            else:
                on_bridge.append(0)
                truck_weights.appendleft(start_truck)
            if bridge_length == len(on_bridge):
                bridge_weight -= on_bridge.popleft()
        else:
            if bridge_length > len(on_bridge):
                on_bridge.append(0)
            elif bridge_length == len(on_bridge):
                if all(i==0 for i in on_bridge):
                    return answer-1
                else:
                    on_bridge.popleft()
                    on_bridge.append(0)

print(solution(2, 10, [7,4, 5, 6]))
print(solution(100,100,[10, 10, 10, 10, 10, 10, 10, 10, 10, 10]))


'''
해당 문제는 큐(Queue) 자료구조를 사용하여 구현할 수 있습니다. 큐는 먼저 들어온 데이터가 먼저 나가는 FIFO(First In First Out) 방식으로 동작하는 자료구조입니다. 다리에 있는 트럭들의 무게를 큐로 표현하면서 문제를 해결해 보겠습니다.

우선, 트럭이 다리에 올라가 있는 시간을 저장할 변수를 하나 만들어 주어야 합니다. 다리 위에 있는 트럭들의 총 무게를 저장하는 변수도 만들어 주어야 합니다. 그리고, 현재 다리 위에 올라가 있는 트럭들을 저장하기 위한 큐를 만들어 줍니다.

큐의 길이가 다리 길이와 같아지면, 다리에서 트럭이 내려오는 것을 구현해 줘야 합니다. 따라서, 큐의 가장 앞에 있는 트럭을 빼내면서 다리 위 트럭들의 총 무게에서 빠진 트럭의 무게를 빼주면 됩니다.

그리고 대기중인 트럭들을 큐에 넣어주면서 다리가 견딜 수 있는 무게를 초과하지 않도록 체크해 주면 됩니다.

'''
'''
from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = deque([0] * bridge_length)
    truck_weights = deque(truck_weights)
    bridge_weight = 0
    
    while bridge:
        answer += 1
        out_truck = bridge.popleft()
        bridge_weight -= out_truck
        
        if truck_weights:
            if bridge_weight + truck_weights[0] <= weight:
                in_truck = truck_weights.popleft()
                bridge.append(in_truck)
                bridge_weight += in_truck
            else:
                bridge.append(0)
            
    return answer


'''