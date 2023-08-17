def solution(n):
    answer = 1
    a, b = 1, 1
    
    for i in range(n-1):
        answer = a + b
        a, b = b, answer
        
    answer %= 1234567
    
    return answer