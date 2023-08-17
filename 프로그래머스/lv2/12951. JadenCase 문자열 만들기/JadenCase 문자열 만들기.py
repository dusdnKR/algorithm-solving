def solution(s):
    answer = ''
    needUpper = True
    
    for text in s:
        if text == ' ':
            answer += text
            needUpper = True
            continue
        if needUpper:
            answer += text.upper()
            needUpper = False
        else:
            answer += text.lower()
    
    return answer