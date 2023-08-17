def solution(name, yearning, photo):
    answer = []
    score = dict(zip(name, yearning))
    for photoNum in photo:
        sum = 0
        for personInPhoto in photoNum:
            if personInPhoto in score:
                sum = sum + score[personInPhoto]
        answer.append(sum)
    return answer