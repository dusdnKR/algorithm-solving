def solution(participant, completion):
    from collections import Counter
    
    participants = Counter(participant)
    completions = Counter(completion)
    
    for person in participants:
        if participants[person] != completions[person]:
            return person