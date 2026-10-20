def solution(phone_book):
    from collections import Counter
    
    phone_counter = Counter(phone_book)
    length = sorted(list(set(len(phone) for phone in phone_book)))
    answer = True
    
    for l in length:
        length_counter = Counter(phone[:l] for phone in phone_book)
        for phone in length_counter:
            if length_counter[phone] >= 2 and phone in phone_counter:
                answer = False
                return answer
    
    return answer