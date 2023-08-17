def solution(s):
    numList = []
    string = ''
    
    for i in s.split():
        numList.append(int(i))
    
    answer = str(min(numList)) + ' ' + str(max(numList))
    
    return answer