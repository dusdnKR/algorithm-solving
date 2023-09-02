def convert_num(n):
    if n == 1: return 1
    elif n == 2: return 2
    else: return 4

def solution(n):
    answer = []
    while n >= 3:
        answer.append(convert_num(n%3))
        n = (n-1) // 3
    if n > 0: answer.append(convert_num(n))

    answer = ''.join(map(str, answer[::-1]))
    
    return answer