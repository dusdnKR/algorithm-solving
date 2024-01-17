def solution(arr):
    
    if len(arr) == 1:
        arr = [-1]
    else:
        arr.remove(sorted(arr)[0])
    
    return arr