def solution(target):
    
    word = []
    target = list(target)
    answer = 0
    
    while word != target:
        if len(word) < 5: word.append("A")
        elif word[-1] == "A": word[-1] = "E"
        elif word[-1] == "E": word[-1] = "I"
        elif word[-1] == "I": word[-1] = "O"
        elif word[-1] == "O": word[-1] = "U"
        else:
            while word[-1] == "U":
                del word[-1]
            if word[-1] == "A": word[-1] = "E"
            elif word[-1] == "E": word[-1] = "I"
            elif word[-1] == "I": word[-1] = "O"
            elif word[-1] == "O": word[-1] = "U"
            
        answer += 1
        
    return answer