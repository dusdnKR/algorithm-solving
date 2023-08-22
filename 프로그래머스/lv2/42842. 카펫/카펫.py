def solution(brown, yellow):
    answer = []
    
    x, y = 0, 0
    total = brown + yellow
    
    for y in range(1, total+1):
        if total % y == 0:
            x = total / y
            if 2*x + 2*y - 4 == brown and (x-2) * (y-2) == yellow:
                answer = [x, y]
                break
        else: continue
    
    return answer