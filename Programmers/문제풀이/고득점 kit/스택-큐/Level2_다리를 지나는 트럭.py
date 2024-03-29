from collections import deque

def solution(bridge_length, weight, truck_weights):
    
    answer = 0

    q = deque(truck_weights)
    temp = []
    temp.append([q.popleft(), 0])
    
    while True:
        
        # tem 가 빈 값이라면, 리턴
        if not temp:
            return answer
        
        answer += 1
    
        # 기존의 temp 에 있던 트럭들은 1만큼 더 이동한다.
        for idx, v in enumerate(temp):
            v[1] += 1
        
        # 이동된 값들에 대해서 트럭이 다리를 통과했으면, temp 에서 제거해준다.
        for idx, v in enumerate(temp):
            if v[1] > bridge_length:
                temp.pop(idx)
        
        print('33~~ {}, {}'.format(temp, answer))
          
        # 만약 q, 즉 트럭이 남아있다면          
        if q:
            t = q.popleft()
            
            # temp 의 트럭 무게들의 합 + 현재의 트럭 무게가 한계무게보다 작다면
            if weight >= sum([x[0] for x in temp]) + t:
                
                # temp 에 새로운 트럭과 1의 이동(다리에 입장)을 추가
                temp.append([t, 1])
                print('11~~ {}, {}'.format(temp, answer))
                
            # 만약 합친 값이 한계무게 보다 크면 q에 다시 그 값을 추가해준다.
            else: 
                print('12~~ {}, {}'.format(temp, answer))
                q.appendleft(t)

            
# bridge_length=2
# weight=10
# truck_weights=[7,4,5,6]

bridge_length=100
weight=100
truck_weights=[10,10,10,10,10,10,10,10,10,10]

print(solution(bridge_length, weight, truck_weights))
