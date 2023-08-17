def solution(s):
    numList = []
    string = ''
    
    for i in s:
        if i != ' ':
            string += i
        else:
            numList.append(int(string))
            string = ''
    numList.append(int(string))
    
    answer = str(min(numList)) + ' ' + str(max(numList))
    
    return answer