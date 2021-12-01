def winRate(win, draw, lose, goal):
    try:
        win = int(win)
        draw = int(draw)
        lose = int(lose)
        currentGames = win + draw + lose

        if currentGames == 0:
            return "현재 승률은 0% 입니다."
        return '현재 승률은 ' + str(round((win / currentGames) * 100, 2)) + '% 입니다.'
    except:
        return "오류입니다."

def winPoint(win, draw, lose, goal):
    try:
        win = int(win)
        draw = int(draw)

        return '현재 승점은 ' + str(3 * win + draw) + '점 입니다.'
    except:
        return "오류입니다."

def goalWinRate(win, draw, lose, goalRate):
    try:
        if float(goalRate) < 0:
            return "0 이상의 수를 입력해주세요."

        win = int(win)
        draw = int(draw)
        lose = int(lose)
        goalRate = float(goalRate)

        goalRate /= 100
        games = 38
        countWin = 0
        currentGames = win + draw + lose
        leaveGames = games - currentGames
        currentRate = (win + countWin) / games

        if goalRate > 1:
            return '최대 승률은 100% 입니다.'
        if goalRate <= currentRate:
            return '이미 목표 승률에 도달했습니다.'

        while currentRate < goalRate:
            countWin += 1
            currentRate = (win + countWin) / games
            if countWin > leaveGames:
                return "목표 승률에 도달할 수 없습니다."
        return '남은 ' + str(leaveGames) +'경기에서 최소 ' + str(countWin) + '승은 더 해야 \n' \
               '목표 승률에 도달할 수 있습니다.\n' + \
               str(win + countWin) + "승 " + str(draw) + "무 " + str(lose + leaveGames - countWin) +\
               "패를 하면 " + str(round(currentRate*100,2)) + "%의 승률을 달성합니다."
    except:
        if goalRate == '':
            return "목표 승률을 입력해주세요."
        if goalRate != int:
            return "숫자를 입력해주세요."
        else:
            return "오류입니다."

def goalWinPoint(win, draw, lose, goalPoint):
    try:
        if float(goalPoint) < 0:
            return "0 이상의 수를 입력해주세요."

        win = int(win)
        draw = int(draw)
        lose = int(lose)
        goalPoint = float(goalPoint)

        games = 38
        countWin = 0
        countDraw = 0
        currentGames = win + draw + lose
        leaveGames = games - currentGames
        currentPoint = 3 * (win + countWin) + (draw + countDraw)

        if goalPoint <= currentPoint:
            return '이미 목표 승점에 도달했습니다.'
        if goalPoint > 114:
            return '최대 획득 가능 승점은 114점 입니다.'
        goalPoint -= currentPoint
        countWin = goalPoint // 3
        countDraw = goalPoint % 3

        if (countWin + countDraw) > leaveGames:
            return "목표 승점에 도달할 수 없습니다."

        while ((countWin + countDraw) <= leaveGames - 2) and (countWin >= 1):
            countWin -= 1
            countDraw += 3

        return '남은 ' + str(leaveGames) +'경기에서 최소 ' + str(int(countWin)) + '승 ' + str(int(countDraw)) + \
               '무를 하면 \n목표 승점에 도달할 수 있습니다.\n' \
               '최소 ' + str(win + int(countWin)) + '승 ' + str(draw + int(countDraw)) + '무 ' + \
               str(games - (win + int(countWin)) - (draw + int(countDraw))) + '패를 해야합니다.'
    except:
        if goalPoint == '':
            return "목표 승점을 입력해주세요."
        if goalPoint != int:
            return "숫자를 입력해주세요."
        else:
            return "오류입니다."