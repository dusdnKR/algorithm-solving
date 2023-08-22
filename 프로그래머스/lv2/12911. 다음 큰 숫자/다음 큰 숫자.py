def solution(n):
    answer = n

    num = list(bin(n))
    numOfOne = num.count('1')
    
    while(True):
        answer += 1
        ans = list(bin(answer))
        numOfOne_ans = ans.count('1')
        
        if numOfOne == numOfOne_ans:
            return answer