def solution(wallpaper):
    answer = []
    lux, luy, rdx, rdy = 50, 50, 0, 0
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[0])):
            if wallpaper[i][j] == '#':
                if i < lux:
                    lux = i
                if j < luy:
                    luy = j
                if i > rdx:
                    rdx = i
                if j > rdy:
                    rdy = j
    answer = [lux, luy, rdx+1, rdy+1]
    return answer