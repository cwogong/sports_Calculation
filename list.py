import soccer
import baseball
import basketball

soccerMap = [
    ('축구 : 현재 승률 계산', soccer.winRate),
    ('축구 : 현재 승점 계산', soccer.winPoint),
    ('축구 : 목표 승률 계산', soccer.goalWinRate),
    ('축구 : 목표 승점 계산', soccer.goalWinPoint),
]

baseballMap = [
    ('야구 : 현재 승률 계산', baseball.winRate),
    ('야구 : 목표 승률 계산', baseball.goalWinRate),
    ('야구 : 게임 차 계산', baseball.gamePointCalc),
]

basketballMap = [
    ('농구 : 현재 승률 계산', basketball.winRate),
    ('농구 : 목표 승률 계산', basketball.goalWinRate),
    ('농구 : 게임 차 계산', basketball.gamePointCalc),
]

helpMap = [
    ("축구 : 도움말", "[현재 승점 계산]은 1승 = 3점, 1무 = 1점, 1패 = 0점을 \n" \
            "\t기준으로 현재 승점을 계산합니다.\n\n" \
            "[현재 승률 계산]은 승 ÷ (승 + 무 + 패) 로 구합니다.\n\n" \
            "[목표 승점 계산]은 남은 경기를 모두 진행한다고 가정할 때, \n" \
            "\t몇 승 몇 무를 더 해야 목표 승점에 도달하는지를 보여줍니다.\n" \
            "\t(1승 2패 = 3무) 로 계산합니다\n\n"\
            "[목표 승률 계산]은 남은 경기를 모두 진행했다고 가정할 때, \n" \
            "\t 몇 승을 더 해야 목표 승률에 도달하는지를 보여줍니다."),
    ("야구 : 도움말", "[현재 승률 계산]은 (승 ÷ 패) 로 구합니다. \n" \
            "\t무승부는 승률 계산에 포함되지 않습니다.\n\n" \
            "[목표 승률 계산]은 남은 경기를 모두 진행했다고 가정할 때, \n" \
            "\t몇 승을 더 해야 목표 승률에 도달하는지를 보여줍니다.\n" \
            "\t(무승부는 없다고 가정합니다.)\n\n" \
            "[게임 차 계산]은 ((승 - 패) - (상대 승 - 상대 패)) ÷ 2 입니다. \n" \
            "\t음수일 경우 상대 팀이 내 팀보다 앞서있는 것을 의미합니다."),
    ("농구 : 도움말", "[현재 승률 계산]은 (승 ÷ 패) 로 구합니다. \n\n" \
            "[목표 승률 계산]은 남은 경기를 모두 진행했다고 가정할 때, \n" \
            "\t몇 승을 더 해야 목표 승률에 도달하는지를 보여줍니다.\n\n" \
            "[게임 차 계산]은 ((승 - 패) - (상대 승 - 상대 패)) ÷ 2 입니다. \n" \
            "\t음수일 경우 상대 팀이 내 팀보다 앞서있는 것을 의미합니다."),
]

soccerList = [x[0] for x in soccerMap]
baseballList = [x[0] for x in baseballMap]
basketballList = [x[0] for x in basketballMap]
helpList = [x[0] for x in helpMap]
