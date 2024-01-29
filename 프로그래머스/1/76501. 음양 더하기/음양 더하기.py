def solution(absolutes, signs):
    
    answer = 0
    
    for sign, num in zip(signs, absolutes):
        if sign == True:
            answer += num
        else:
            answer -= num
    
    return answer