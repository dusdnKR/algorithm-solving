def solution(s): 
    
    numOfZero = 0
    numOfConversion = 0
    
    while s != '1':
        numOfZero += s.count('0')
        s = s.replace('0', '')
        
        s = format(len(s), 'b')
        
        numOfConversion += 1
    
    answer = [numOfConversion, numOfZero]
    
    return answer