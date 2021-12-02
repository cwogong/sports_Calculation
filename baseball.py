def winRate(win, draw, lose, win2, draw2, lose2, goal):
    try:
        win = int(win)
        lose = int(lose)
        currentGames = win + lose

        if currentGames == 0:
            return "현재 승률은 0% 입니다."
        return '내 팀의 현재 승률은 ' + str(round((win / currentGames) * 100, 2)) + '% 입니다.'
    except:
        return "오류입니다."

def goalWinRate(win, draw, lose, win2, draw2, lose2, goalRate):
    try:
        if float(goalRate) < 0:
            return "0 이상의 수를 입력해주세요."

        win = int(win)
        draw = int(draw)
        lose = int(lose)
        goalRate = float(goalRate)

        goalRate /= 100
        games = 144
        countWin = 0
        currentGames = win + draw + lose
        leaveGames = games - currentGames
        currentRate = (win + countWin) / (games - draw)

        if goalRate > 1:
            return '최대 승률은 100% 입니다.'
        if goalRate <= currentRate:
            return '이미 목표 승률에 도달했습니다.'

        while currentRate < goalRate:
            countWin += 1
            currentRate = (win + countWin) / (games - draw)
            if countWin > leaveGames:
                return "목표 승률에 도달할 수 없습니다."
        return '남은 ' + str(leaveGames) +'경기에서 최소 ' + str(countWin) + '승은 해야 \n목표 승률에 도달할 수 있습니다.\n' + \
               str(win + countWin) + "승 " + str(draw) + "무 " + str(lose + leaveGames - countWin) + \
               "패를 하면 " + str(round(currentRate * 100, 2)) + "%의 승률을 달성합니다."

    except:
        if goalRate == '':
            return "목표 승률을 입력해주세요."
        if goalRate != int:
            return "숫자를 입력해주세요."
        else:
            return "오류입니다."

def gamePointCalc(win, draw, lose, win2, draw2, lose2, goal):
    try:
        if win2 == '' or draw2 == '' or lose2 == '':
            return "우리 팀과 상대 팀의 승, 무, 패를 모두 입력해주세요."
        if int(win2) + int(draw2) + int(lose2) > 144:
            return "야구의 최대 경기 수는 144경기입니다."
        if int(win2) < 0 or int(draw2) < 0 or int(lose2) < 0:
            return "0 이상의 수를 입력해주세요."

        win = int(win)
        lose = int(lose)
        win2 = int(win2)
        lose2 = int(lose2)

        gamePoint = ((win - lose) - (win2 - lose2)) * 0.5

        if gamePoint > 0:
            return '내 팀이 상대 팀보다 ' + str(gamePoint) + '게임 차로 앞서있습니다.'
        elif gamePoint < 0:
            return '내 팀이 상대 팀보다 ' + str(abs(gamePoint)) + '게임 차로 뒤쳐져있습니다.'
        else:
            return '내 팀과 상대 팀의 게임 차가 없습니다.'
    except:
        return "오류입니다."

baseballMap = [
    ('야구 : 현재 승률 계산', winRate),
    ('야구 : 목표 승률 계산', goalWinRate),
    ('야구 : 게임 차 계산', gamePointCalc),
]
baseballList = [x[0] for x in baseballMap]