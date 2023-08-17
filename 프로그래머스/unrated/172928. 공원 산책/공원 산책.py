def solution(park, routes):
    answer = []
    location = []
    
    for i, string in enumerate(park):
        if string.find('S') >= 0:
            location = [i, string.find('S')]
            break
        
    H = len(park)
    W = len(park[0])
    
    for route in routes:
        if route[0] == 'E':
            move = True
            for i in range(1, int(route[2])+1):
                newLoc = [location[0], location[1]+i]
                if 0 <= newLoc[0] < H and 0 <= newLoc[1] < W:
                    if park[newLoc[0]][newLoc[1]] == 'X':
                        move = False
                        break
                else:
                    move = False
                    break
            if move:
                location[1] += int(route[2])
                
        elif route[0] == 'W':
            move = True
            for i in range(1, int(route[2])+1):
                newLoc = [location[0], location[1]-i]
                if 0 <= newLoc[0] < H and 0 <= newLoc[1] < W:
                    if park[newLoc[0]][newLoc[1]] == 'X':
                        move = False
                        break
                else:
                    move = False
                    break
            if move:
                location[1] -= int(route[2])
                
        elif route[0] == 'S':
            move = True
            for i in range(1, int(route[2])+1):
                newLoc = [location[0]+i, location[1]]
                if 0 <= newLoc[0] < H and 0 <= newLoc[1] < W:
                    if park[newLoc[0]][newLoc[1]] == 'X':
                        move = False
                        break
                else:
                    move = False
                    break
            if move:
                location[0] += int(route[2])
                
        elif route[0] == 'N':
            move = True
            for i in range(1, int(route[2])+1):
                newLoc = [location[0]-i, location[1]]
                if 0 <= newLoc[0] < H and 0 <= newLoc[1] < W:
                    if park[newLoc[0]][newLoc[1]] == 'X':
                        move = False
                        break
                else:
                    move = False
                    break
            if move:
                location[0] -= int(route[2])
                
    answer = location
    return answer