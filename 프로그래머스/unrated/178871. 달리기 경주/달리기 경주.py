def solution(players, callings):
    answer = []
    playersRank = []
    for i in range(1, len(players) + 1):
        playersRank.append(i)
    rankAndName = dict(zip(playersRank, players))
    nameAndRank = dict(zip(players, playersRank))
    for currPlayer in callings:
        currRank = nameAndRank[currPlayer]
        frontPlayer = rankAndName[currRank - 1]
        rankAndName[currRank - 1], rankAndName[currRank] = rankAndName[currRank], rankAndName[currRank - 1]
        nameAndRank[frontPlayer], nameAndRank[currPlayer] = nameAndRank[currPlayer], nameAndRank[frontPlayer]
    for player in rankAndName.values():
        answer.append(player)
    return answer