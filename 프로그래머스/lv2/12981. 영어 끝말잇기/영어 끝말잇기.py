def solution(n, words):
    answer = [0, 0]
    log = []
    
    for i, word in enumerate(words):
        if i == 0:
            log.append(word)
            continue
        else:
            if words[i-1][-1] != word[0] or word in log:
                answer = [(i+1)%n, (i+1)/n]
                if answer[0] == 0:
                    answer[0] = n
                if answer[1] % 1 != 0:
                    answer[1] = int(answer[1])+1
                break
            log.append(word)
    
    return answer