import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QGridLayout, QWidget,QPushButton
from PyQt5.QtGui import QPixmap, QImage,QFont
from PyQt5.QtCore import QTimer
c =0
class window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(500,300,700,500)
        self.setWindowTitle("StopWatch")
        self.label = QLabel(self)
        self.label.setGeometry(250,100,250,300)
        self.label.setText("0")
        self.label.setFont(QFont("Arial",60,QFont.Bold))
        
        self.timer=QTimer(self)
        self.timer.timeout.connect(self.run)
        self.totaltime = 0

        self.startBtn = QPushButton(self)
        self.startBtn.setText("Start/Stop")
        self.resetBtn = QPushButton(self)
        self.resetBtn.setText("Reset")


        self.startBtn.clicked.connect(self.StopCount)
        self.startBtn.setGeometry(100,400,100,50)
        self.resetBtn.clicked.connect(self.resetCount)
        self.resetBtn.setGeometry(200,400,100,50)
        
    def StopCount(self):
        global c
        if (c ==0):
            self.timer.start(100)
            c = 1
        else:
            self.timer.stop()
            c =0
            
    def resetCount(self):
        self.totaltime = 0
        self.label.setText("0")
        self.timer.stop()

    def run(self):
        self.label.setText(str(self.totaltime))
        self.totaltime+=0.1


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = window()
    ex.show()
    sys.exit(app.exec_())