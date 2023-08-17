def solution(order):
    answer = 0
    subContainer = []
    box = 1
    
    for box in range(1, len(order)+1):
        subContainer.append(box)
        while subContainer and subContainer[-1] == order[answer]:
            del subContainer[-1]
            answer += 1
        
    return answer