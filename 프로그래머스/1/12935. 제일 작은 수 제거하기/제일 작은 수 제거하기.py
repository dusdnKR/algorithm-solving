def solution(arr):
    
    arr.remove(sorted(arr)[0])
    
    if arr:
        return arr
    else:
        return [-1]