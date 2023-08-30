def solution(numbers, target):
    answer = 0
    
    binary = 2 ** (len(numbers))
    binary_list = bin(binary)
    binary_list = list(binary_list[3:])
    binary_list[0] = '0'
    
    while '0' in binary_list:
        total = 0
        for i, num in enumerate(numbers):
            if binary_list[i] == '0':
                total += num
            else:
                total -= num
        if total == target:
            answer += 1
        binary += 1
        binary_list = bin(binary)
        binary_list = list(binary_list[3:])
    
    return answer