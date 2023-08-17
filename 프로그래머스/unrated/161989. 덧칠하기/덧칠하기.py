def solution(n, m, section):
    
    answer = 1
    start = section[0]
    
    for location in section:
        end = start + m - 1
        if location <= end:
            continue
        else:
            start = location
            answer += 1
    
    return answer