def solution(operations):
    answer = [0, 0]
    queue = []
    
    for i in operations:
        if i[0] == "I":
            queue.append(int(i[2:]))
        elif i == "D 1":
            if queue: queue.remove(max(queue))
        else:
            if queue: queue.remove(min(queue))
    
    if queue: answer = [max(queue), min(queue)]
    
    return answer