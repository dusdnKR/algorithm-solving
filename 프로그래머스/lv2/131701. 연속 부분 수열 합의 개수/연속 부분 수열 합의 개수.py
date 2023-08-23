def solution(elements):
    answer = 0
    numOfElements = len(elements)
    sumOfElements = 0
    sumList = []
    
    elements += elements
    
    for n in range(1, numOfElements+1):
        for m in range(numOfElements):
            sumOfElements = sum(elements[m:m+n])
            sumList.append(sumOfElements)
    
    answer = len(set(sumList))
    
    return answer
