def solution(n):
    answer = 0
    
    f1, f2, f3 = 0, 1, 1
    
    for i in range(n-1):
        f3 = f1 + f2
        f1 = f2
        f2 = f3
    
    answer = f3 % 1234567
    
    return answer