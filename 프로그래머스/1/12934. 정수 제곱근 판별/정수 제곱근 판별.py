def solution(n):
    
    rootN = n**(1/2)
    
    if int(rootN)**2 == n:
        return (int(rootN)+1)**2
    else:
        return -1