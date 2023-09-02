def dfs(k, dungeons, depth, visited):
    MAX = depth
    if depth == len(dungeons):
        return depth
    for dungeon in dungeons:
        if k >= dungeon[0] and dungeon not in visited:
            visited.append(dungeon)
            MAX = max(MAX, dfs(k-dungeon[1], dungeons, depth+1, visited))
            visited.remove(dungeon)
    return MAX
        
def solution(k, dungeons):
    answer = -1
    visited = []
    answer = dfs(k, dungeons, 0, visited)
    return answer