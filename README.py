# E5from PyQt5.QtGui import QCursor
from PyQt5.Qt import QLCDNumber,QPushButton,QTextEdit,Qt,QTimer
import sys
from PyQt5.QtWidgets import QWidget,QApplication,QStyleFactory

class Timer(QWidget):
    def __init__(self):
        super(Timer, self).__init__()
        self.setWindowTitle('秒表')
        self.resize(420,480)
        self.setWindowFlags(Qt.FramelessWindowHint)
        #窗口无边框化
        self.lcd = QLCDNumber(self)
        self.lcd.setDigitCount(10)
        self.lcd.setMode(QLCDNumber.Dec)
        self.lcd.setSegmentStyle(QLCDNumber.Flat)
        self.min=0
        self.sec=0
        self.secondSec=0
        
        self.linetext=str(0)+str(self.min)+':'+str(0)+str(self.sec)+':'+str(0)+str(self.secondSec)
        self.lcd.display(self.linetext)#在lcd上显示当前时间
        self.lcd.setGeometry(40,70,300,100)


        self.startButton=QPushButton(self)
        self.startButton.setText('开始')
        self.stopButton=QPushButton(self)
        self.stopButton.setText('停止')
        self.resetButton=QPushButton(self)
        self.resetButton.setText('复位')
        self.exitButton = QPushButton(self)
        self.exitButton.setText('退出')


        self.startButton.setCursor(QCursor(Qt.PointingHandCursor))#鼠标一上去按钮变手性
        self.stopButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.resetButton.setCursor(QCursor(Qt.PointingHandCursor))

        self.textEdit=QTextEdit(self)
        self.textEdit.setGeometry(40,200,300,200)

        self.startButton.setGeometry(50,20,80,30)
        self.stopButton.setGeometry(150,20,80,30)
        self.resetButton.setGeometry(250,20,80,30)
        self.exitButton.setGeometry(260, 420, 80, 30)

        self.timer = QTimer()
        self.timer.setInterval(10)

        self.timer.timeout.connect(self.onTimerOut)

        self.startButton.clicked.connect(self.start)
        self.stopButton.clicked.connect(self.stop)
        self.resetButton.clicked.connect(self.reset)
        self.exitButton.clicked.connect(self.exit)

        self.count=1


    def onTimerOut(self):
        self.secondSec+=1
        if self.secondSec!=100:
            if self.secondSec<10 and self.sec<10 :
                self.linetext=str(0) + str(self.min) + ':' + str(0) + str(self.sec) + ':' + str(0) + str(self.secondSec)
                self.lcd.display(self.linetext)
            elif self.secondSec>=10 and self.sec<10 :
                self.linetext=str(0) + str(self.min) + ':' +str(0) + str(self.sec) + ':' + str(self.secondSec)
                self.lcd.display(self.linetext)
            elif self.secondSec <10 and self.sec >=10:
                self.linetext=str(0) + str(self.min) + ':'+str(self.sec) + ':' + str(0)+str(self.secondSec)
                self.lcd.display(self.linetext)
            elif self.secondSec >= 10 and self.sec >=10:
                self.linetext=str(0) + str(self.min) + ':' +str(self.sec) + ':' + str(self.secondSec)
                self.lcd.display(self.linetext)

        if self.secondSec==100:
            self.secondSec=0
            self.sec+=1

        if self.sec==60:
            self.sec=0
            self.min+=1

    def start(self):
        self.timer.start()
        if self.startButton.text()=='计次':
            self.textEdit.append('计次'+str(self.count)+'      '+self.linetext)
            self.count+=1
        self.startButton.setText('计次')


    def stop(self):
        self.timer.stop()
        self.startButton.setText('继续')

    def reset(self):
        self.timer.stop()
        self.sec=0
        self.min=0
        self.lcd.display(str(0)+str(0)+':'+str(0)+str(0)+':'+str(0)+str(0))
        self.startButton.setText('开始')
        self.textEdit.clear()
        self.count=1

    def exit(self):
        sys.exit(app.exec())


if __name__ == '__main__':
    app=QApplication(sys.argv)
    app.setStyle(QStyleFactory.create("Fusion"))#设置窗口界面
    main = Timer()
    qssStyle = '''
                QPushButton{
                    background-color: rgb(44, 137, 255);     
                    }
       '''

    main.setStyleSheet(qssStyle)
    main.show()
    sys.exit(app.exec())
