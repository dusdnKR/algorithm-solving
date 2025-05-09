def solution(babbling):
    answer = 0
    library = ["aya", "ye", "woo", "ma"]
    
    for babb in babbling:
        lib0 = babb.count(library[0])
        lib1 = babb.count(library[1])
        lib2 = babb.count(library[2])
        lib3 = babb.count(library[3])
        
        length = lib0*len(library[0]) + lib1*len(library[1]) + lib2*len(library[2]) + lib3*len(library[3])
        
        if lib0 < 2 and lib1 < 2 and lib2 < 2 and lib3 < 2 and length == len(babb):
            answer += 1
    
    return answer