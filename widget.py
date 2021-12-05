from PyQt5.QtCore import QLine
from PyQt5.QtWidgets import (QGridLayout, QGroupBox, QComboBox, QMessageBox, QPushButton, QSizePolicy,
                             QHBoxLayout, QVBoxLayout, QBoxLayout, QLabel, QTextEdit, QLineEdit,)
from help import helpMap, helpList
from soccer import soccerMap, soccerList
from baseball import baseballMap, baseballList
from basketball import basketballMap, basketballList
import datetime
import baseballRanking, soccerRanking, basketballRanking

class Button(QPushButton):
    def __init__(self, text, callback):
        super().__init__()
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        self.setFixedSize(150, 30)
        self.setText(text)
        self.clicked.connect(callback)

class Widget(QGroupBox):
    def __init__(self):
        QGroupBox.__init__(self)
        self.box = QBoxLayout(QBoxLayout.TopToBottom)
        self.setLayout(self.box)

        self.winEdit = QLineEdit()
        self.winEdit2 = QLineEdit()
        self.drawEdit = QLineEdit()
        self.drawEdit2 = QLineEdit()
        self.loseEdit = QLineEdit()
        self.loseEdit2 = QLineEdit()
        self.goalEdit = QLineEdit()

        self.rankEdit = QLineEdit()

        self.clearButton = Button("초기화", self.clearButtonClicked)
        self.clearButton.setFixedSize(100, 30)

    def clearButtonClicked(self):
        self.winEdit.setText("")
        self.winEdit2.setText("")
        self.drawEdit.setText("")
        self.drawEdit2.setText("")
        self.loseEdit.setText("")
        self.loseEdit2.setText("")
        self.goalEdit.setText("")
        self.display.setText("")

    def helpButtonClicked(self):
        button = self.sender()
        key = button.text()
        txt = helpMap[helpList.index(key)][1]
        QMessageBox.information(self, "도움말", txt)

class SoccerWidget(Widget):
    def __init__(self):
        super(SoccerWidget, self).__init__()
        self.setTitle("축구 (38경기)")

        self.helpButton = Button("축구 : 도움말", self.helpButtonClicked)
        self.helpButton.setFixedSize(100, 30)

        dic = (
            {'name': self.winEdit, 'label': '승 :'},
            {'name': self.drawEdit, 'label': '무 :'},
            {'name': self.loseEdit, 'label': '패 :'},
            {'name': self.goalEdit, 'label': '목표 승점(승률) :'}
        )

        for i in dic:
            hbox = QHBoxLayout()
            hbox.addWidget(QLabel(i['label']))
            hbox.addWidget(i['name'])
            if i['label'] == '목표 승점(승률) :':
                hbox.addWidget(QLabel("점, %"))
            self.box.addLayout(hbox)

        hbox = QHBoxLayout()
        cnt = 0
        for i in soccerList:
            button = Button(i,self.buttonClicked)
            hbox.addWidget(button)
            cnt += 1
            if cnt == 2:
                self.box.addLayout(hbox)
                hbox = QHBoxLayout()
        self.box.addLayout(hbox)

        self.display = QTextEdit()
        self.display.setReadOnly(True)
        self.display.setFixedHeight(100)
        self.box.addWidget(self.display)

        hbox = QHBoxLayout()
        hbox.addWidget(self.clearButton)
        hbox.addStretch()
        hbox.addWidget(self.helpButton)
        self.box.addLayout(hbox)

    def buttonClicked(self):
        button = self.sender()
        key = button.text()

        win = self.winEdit.text()
        draw = self.drawEdit.text()
        lose = self.loseEdit.text()
        goal = self.goalEdit.text()

        if win == '' or draw == '' or lose == '':
            self.display.setText('승리, 무승부, 패배를 모두 입력해주세요.')
            return
        try:
            if int(win) + int(draw) + int(lose) > 38:
                self.display.setText("축구의 최대 경기 수는 38경기 입니다.")
                return
            if int(win) < 0 or int(draw) < 0 or int(lose) < 0:
                self.display.setText("0 이상의 수를 입력해주세요.")
                return
        except:
            self.display.setText("숫자를 입력해주세요.")
            return

        value = soccerMap[soccerList.index(key)][1](win, draw, lose, goal)
        self.display.setText(str(value))

class BaseballWidget(Widget):
    def __init__(self):
        super(BaseballWidget, self).__init__()
        self.setTitle("야구 (144경기)")

        self.helpButton = Button("야구 : 도움말", self.helpButtonClicked)
        self.helpButton.setFixedSize(100, 30)

        hbox = QHBoxLayout()
        hbox.addWidget(QLabel("내 팀"))
        hbox.addWidget(QLabel("상대 팀"))
        self.box.addLayout(hbox)

        dic = (
            {'name': self.winEdit, 'label': '승 :'},
            {'name': self.winEdit2, 'label': ', 승 :'},
            {'name': self.drawEdit, 'label': '무 :'},
            {'name': self.drawEdit2, 'label': ', 무 :'},
            {'name': self.loseEdit, 'label': '패 :'},
            {'name': self.loseEdit2, 'label': ', 패 :'},
            {'name': self.goalEdit, 'label': '목표 승률 :'}
        )

        for i in range(0, len(dic), 2):
            hbox = QHBoxLayout()
            hbox.addWidget(QLabel(dic[i]['label']))
            hbox.addWidget(dic[i]['name'])
            if dic[i]['label'] == '목표 승률 :':
                hbox.addWidget(QLabel("%"))
            else:
                hbox.addWidget(QLabel(dic[i + 1]['label']))
                hbox.addWidget(dic[i + 1]['name'])
            self.box.addLayout(hbox)

        hbox = QHBoxLayout()
        cnt = 0
        for i in baseballList:
            button = Button(i, self.buttonClicked)
            hbox.addWidget(button)
            cnt += 1
            if cnt == 2:
                self.box.addLayout(hbox)
                hbox = QHBoxLayout()
        self.box.addLayout(hbox)

        self.display = QTextEdit()
        self.display.setReadOnly(True)
        self.display.setFixedHeight(100)
        self.box.addWidget(self.display)

        hbox = QHBoxLayout()
        hbox.addWidget(self.clearButton)
        hbox.addStretch()
        hbox.addWidget(self.helpButton)
        self.box.addLayout(hbox)

    def buttonClicked(self):
        button = self.sender()
        key = button.text()

        win = self.winEdit.text()
        win2 = self.winEdit2.text()
        draw = self.drawEdit.text()
        draw2 = self.drawEdit2.text()
        lose = self.loseEdit.text()
        lose2 = self.loseEdit2.text()
        goal = self.goalEdit.text()

        if win == '' or draw == '' or lose == '':
            self.display.setText('내 팀의 승리, 무승부, 패배를 모두 입력해주세요.')
            return
        try:
            if int(win) + int(draw) + int(lose) > 144:
                self.display.setText("야구의 최대 경기 수는 144경기입니다.")
                return
            if int(win) < 0 or int(draw) < 0 or int(lose) < 0:
                self.display.setText("0 이상의 수를 입력해주세요.")
                return
        except:
            self.display.setText("숫자를 입력해주세요.")
            return

        value = baseballMap[baseballList.index(key)][1](win, draw, lose, win2, draw2, lose2, goal)
        self.display.setText(str(value))

class BasketballWidget(Widget):
    def __init__(self):
        super(BasketballWidget, self).__init__()
        self.setTitle("농구 (54경기)")

        self.helpButton = Button("농구 : 도움말", self.helpButtonClicked)
        self.helpButton.setFixedSize(100, 30)

        hbox = QHBoxLayout()
        hbox.addWidget(QLabel("내 팀"))
        hbox.addWidget(QLabel("상대 팀"))
        self.box.addLayout(hbox)

        dic = (
            {'name': self.winEdit, 'label': '승 :'},
            {'name': self.winEdit2, 'label': ', 승 :'},
            {'name': self.loseEdit, 'label': '패 :'},
            {'name': self.loseEdit2, 'label': ', 패 :'},
            {'name': self.goalEdit, 'label': '목표 승률 :'}
        )

        for i in range(0, len(dic), 2):
            hbox = QHBoxLayout()
            hbox.addWidget(QLabel(dic[i]['label']))
            hbox.addWidget(dic[i]['name'])
            if dic[i]['label'] == '목표 승률 :':
                hbox.addWidget(QLabel("%"))
            else:
                hbox.addWidget(QLabel(dic[i + 1]['label']))
                hbox.addWidget(dic[i + 1]['name'])
            self.box.addLayout(hbox)

        hbox = QHBoxLayout()
        cnt = 0
        for i in basketballList:
            button = Button(i, self.buttonClicked)
            hbox.addWidget(button)
            cnt += 1
            if cnt == 2:
                self.box.addLayout(hbox)
                hbox = QHBoxLayout()
        self.box.addLayout(hbox)

        self.display = QTextEdit()
        self.display.setReadOnly(True)
        self.display.setFixedHeight(100)
        self.box.addWidget(self.display)

        hbox = QHBoxLayout()
        hbox.addWidget(self.clearButton)
        hbox.addStretch()
        hbox.addWidget(self.helpButton)
        self.box.addLayout(hbox)
        
    def buttonClicked(self):
        button = self.sender()
        key = button.text()

        win = self.winEdit.text()
        win2 = self.winEdit2.text()
        lose = self.loseEdit.text()
        lose2 = self.loseEdit2.text()
        goal = self.goalEdit.text()

        if win == '' or lose == '':
            self.display.setText('내 팀의 승리, 패배를 모두 입력해주세요.')
            return
        try:
            if int(win) + int(lose) > 54:
                self.display.setText("농구의 최대 경기 수는 54경기입니다.")
                return
            if int(win) < 0 or int(lose) < 0:
                self.display.setText("0 이상의 수를 입력해주세요.")
                return
        except:
            self.display.setText("숫자를 입력해주세요.")
            return

        value = basketballMap[basketballList.index(key)][1](win, lose, win2, lose2, goal)
        self.display.setText(str(value))

class AdviceWidget(QGroupBox):
    def __init__(self):
        QGroupBox.__init__(self)
        self.box = QBoxLayout(QBoxLayout.TopToBottom)
        self.setLayout(self.box)
        self.setTitle("에러, 건의사항")

        self.nameEdit = QLineEdit()
        self.nameEdit.setPlaceholderText('이름을 입력해주세요.')
        self.content = QTextEdit()
        self.content.setPlaceholderText('내용을 입력해주세요.')
        self.eventType = QComboBox()
        self.eventType.addItem('건의사항')
        self.eventType.addItem('에러')

        hbox = QHBoxLayout()
        hbox.addWidget(QLabel("이름 :"))
        hbox.addWidget(self.nameEdit)
        self.box.addLayout(hbox)

        hbox = QHBoxLayout()
        hbox.addWidget(QLabel("에러 또는 건의사항을 선택 후 적어주세요"))
        hbox.addWidget(self.eventType)
        self.box.addLayout(hbox)
        self.box.addWidget(self.content)
        self.submitButton = Button("제출", self.submitButtonClicked)
        self.box.addWidget(self.submitButton)

    def submitButtonClicked(self):
        if self.eventType.currentText() == '건의사항':
            try:
                fH = open('advice.txt', "a")
            except:
                fH = open('advice.txt', "w")
        else:
            try:
                fH = open('errors.txt', "a")
            except:
                fH = open('errors.txt', "w")
        try:
            date = datetime.datetime.today()
            year = str(date.year)
            month = str(date.month)
            day = str(date.day)
            hour = str(date.hour)
            minute = str(date.minute)

            if self.nameEdit.text() == '' or self.content.toPlainText() == '':
                if self.nameEdit.text() == '':
                    self.nameEdit.setPlaceholderText('이름을 입력해주세요.')
                return

            fH.write('[' + year + "." + month + "." + day + ".(" + hour + ":" + minute + ')]  '
                     + self.nameEdit.text() + '\n' + self.content.toPlainText() + '\n\n')
            font = self.content.font()
            font.setPointSize(font.pointSize() + 4)
            self.content.setFont(font)
            self.content.setText("좋은 의견 감사합니다!")
            self.nameEdit.setText('')
            self.content.setReadOnly(True)
            self.nameEdit.setReadOnly(True)
            self.submitButton.setEnabled(False)
            self.eventType.setEnabled(False)

        except:
            self.content.setText("다시 입력해 주세요.")
            return

class SoccerRankingWidget(QGroupBox):
    def __init__(self):
        QGroupBox.__init__(self)
        self.box = QBoxLayout(QBoxLayout.LeftToRight)
        self.setLayout(self.box)
        self.setTitle("현재 순위")

        label = ["순위", "팀", "경기", "승", "무", "패", "승점"]
        content = [soccerRanking.rank, soccerRanking.team, soccerRanking.games, soccerRanking.wins, soccerRanking.draws, soccerRanking.loses, soccerRanking.points]

        for j in range(len(label)):
            vbox = QVBoxLayout()
            vbox.addWidget(QLabel(label[j]))
            for i in range(len(soccerRanking.team_rank_list)):
                vbox.addWidget(QLabel(str(content[j][i])))
            self.box.addLayout(vbox)

class BaseballRankingWidget(QGroupBox):
    def __init__(self):
        QGroupBox.__init__(self)
        self.box = QBoxLayout(QBoxLayout.LeftToRight)
        self.setLayout(self.box)
        self.setTitle("현재 순위")

        label = ["순위", "팀", "경기", "승", "무", "패", "승률"]
        content = [baseballRanking.rank, baseballRanking.team, baseballRanking.games, baseballRanking.wins, baseballRanking.draws, baseballRanking.loses, baseballRanking.rate]

        for j in range(len(label)):
            vbox = QVBoxLayout()
            vbox.addWidget(QLabel(label[j]))
            for i in range(len(soccerRanking.team_rank_list)):
                vbox.addWidget(QLabel(str(content[j][i])))
            self.box.addLayout(vbox)

class BasketballRankingWidget(QGroupBox):
    def __init__(self):
        QGroupBox.__init__(self)
        self.box = QBoxLayout(QBoxLayout.LeftToRight)
        self.setLayout(self.box)
        self.setTitle("현재 순위")

        label = ["순위", "팀", "경기", "승", "패", "승률"]
        content = [basketballRanking.rank, basketballRanking.team, basketballRanking.games, basketballRanking.wins, basketballRanking.loses, basketballRanking.rate]

        for j in range(len(label)):
            vbox = QVBoxLayout()
            vbox.addWidget(QLabel(label[j]))
            for i in range(len(basketballRanking.team_rank_list)):
                vbox.addWidget(QLabel(str(content[j][i])))
            self.box.addLayout(vbox)

class EmptyWidget(QGroupBox):
    def __init__(self):
        QGroupBox.__init__(self)