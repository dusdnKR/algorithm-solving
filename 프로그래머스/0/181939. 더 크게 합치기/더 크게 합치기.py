def solution(a, b):
    str1 = str(a)+str(b)
    str2 = str(b)+str(a)
    
    answer = str1 if str1 > str2 else str2
    
    return int(answer)