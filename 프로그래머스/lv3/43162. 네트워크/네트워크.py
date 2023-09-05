def solution(n, computers):
    answer = 0
    visited = [False] * n
    for i in range(n):
        if not visited[i]:
            answer += 1
            stack = [i]
            while stack:
                x = stack.pop()
                visited[x] = True
                for j in range(n):
                    if x != j and computers[x][j] == 1 and not visited[j]:
                        stack.append(j)
    
    return answer