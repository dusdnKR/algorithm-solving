def solution(elements):
    sumSet = set()
    n = len(elements)
    
    for i in range(n):
        sumOfElements = 0
        for j in range(i, i+n-1):
            sumOfElements += elements[j%n]
            sumSet.add(sumOfElements)
    
    return len(sumSet) + 1
    
"""
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

def solution(elements):
    answer = 0
    numOfElements = len(elements)
    sumOfElements = 0
    sumSet = set()
    
    for element in elements:
        sumSet.add(element)
        
    sumSet.add(sum(elements))
    
    elements += elements
    
    for n in range(2, numOfElements):
        for m in range(numOfElements):
            sumOfElements = sum(elements[m:m+n])
            sumSet.add(sumOfElements)
    
    answer = len(sumSet)
    
    return answer
"""