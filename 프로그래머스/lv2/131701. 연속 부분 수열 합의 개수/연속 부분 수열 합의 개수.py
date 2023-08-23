def solution(elements):
    answer = 0
    numOfElements = len(elements)
    sumOfElements = 0
    sumList = []
    
    sumList = elements.copy()
    sumList.append(sum(elements))
    
    elements += elements
    
    for n in range(2, numOfElements):
        for m in range(numOfElements):
            sumOfElements = sum(elements[m:m+n])
            sumList.append(sumOfElements)
    
    answer = len(set(sumList))
    
    return answer