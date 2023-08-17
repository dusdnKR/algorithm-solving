def solution(s):
    answer = False
    x = 0
    
    if s[0] == ')':
        return False
    
    for i in s:
        if i == '(':
            x += 1
        else:
            x -= 1
            if x < 0:
                x = 0
    
    if x == 0:
        answer = True
        
    return answer