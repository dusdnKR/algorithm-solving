def solution(numbers, target):
    answer = [0]
    
    def visit(index, total):
        if index == len(numbers):
            if total == target:
                answer[0] += 1
            return
        
        visit(index + 1, total + numbers[index])
        visit(index + 1, total - numbers[index])
    
    visit(0, 0)
    
    return answer[0]