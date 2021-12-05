import sys
from PyQt5.QtWidgets import (QGridLayout, QLabel, QWidget, QStackedWidget, QGroupBox, QListView,
                             QApplication, QBoxLayout, QLayout)
from PyQt5.QtGui import QStandardItem, QStandardItemModel
from widget import SoccerWidget, BaseballWidget, BasketballWidget, AdviceWidget, SoccerRankingWidget, BaseballRankingWidget, BasketballRankingWidget, EmptyWidget

class Main(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.stk_w = QStackedWidget(self)
        self.stk_r = QStackedWidget(self)
        self.init_widget()

    def init_widget(self):
        self.setWindowTitle("Sports Calculation")
        widget_laytout = QBoxLayout(QBoxLayout.LeftToRight)

        group = QGroupBox()
        group.setFixedHeight(250)
        group.setFixedWidth(150)
        box = QBoxLayout(QBoxLayout.TopToBottom)
        group.setLayout(box)
        group.setTitle("종목을 선택해주세요")
        widget_laytout.addWidget(group)

        widgets = ["축구(EPL)", "야구(KBO)", "농구(KBL)", "에러, 건의사항"]
        view = QListView(self)
        font = view.font()
        font.setPointSize(font.pointSize() + 4)
        view.setFont(font)
        model = QStandardItemModel()
        for i in widgets:
            model.appendRow(QStandardItem(i))
        view.setModel(model)
        box.addWidget(view)

        self.stk_w.addWidget(SoccerWidget())
        self.stk_w.addWidget(BaseballWidget())
        self.stk_w.addWidget(BasketballWidget())
        self.stk_w.addWidget(AdviceWidget())

        self.stk_r.addWidget(SoccerRankingWidget())
        self.stk_r.addWidget(BaseballRankingWidget())
        self.stk_r.addWidget(BasketballRankingWidget())
        self.stk_r.addWidget(EmptyWidget())

        widget_laytout.addWidget(self.stk_w)
        widget_laytout.setSizeConstraint(QLayout.SetFixedSize)

        widget_laytout.addWidget(self.stk_r)
        self.setLayout(widget_laytout)

        # 시그널 슬롯 연결
        view.clicked.connect(self.slot_clicked_item)

    def slot_clicked_item(self, idx):
        self.stk_w.setCurrentIndex(idx.row())
        self.stk_r.setCurrentIndex(idx.row())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = Main()
    form.show()
    exit(app.exec_())