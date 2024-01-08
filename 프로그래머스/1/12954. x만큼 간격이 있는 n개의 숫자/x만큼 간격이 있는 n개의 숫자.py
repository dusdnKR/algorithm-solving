def solution(x, n):
    answer = []
    if x != 0:
        for i in range(x, x*n, x):
            answer.append(i)
        answer.append(x*n)
    else:
        for i in range(n):
            answer.append(x)
    return answer