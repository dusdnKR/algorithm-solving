def solution(n):
    answer = 1 # 'n = n'인 경우
    
    for i in range(1, n):
        sum = 0
        j = i
        
        while sum < n:
            sum += j
            j += 1
            
        if sum == n:
            answer += 1
    
    return answer