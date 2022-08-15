import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton
from PyQt5.QtGui import QFont, QIcon

app = QApplication(sys.argv)
win = QWidget()
win.setWindowTitle('Calculator')
win.setWindowIcon(QIcon('calculator\calculator-icon-256-348653001.png'))
win.setStyleSheet("background-color:#fbe29d")
win.setFixedSize(531, 660)
win.move(600, 150)

total = ''
f = QFont("Times New Roman", 20, 10)

e = QLabel('0', win)
e.setFont(f)
e.setStyleSheet("QLabel"
				    "{"
				    "border : 4px solid #002de3;"
				    "background : #fef6e2;"
				    "}")
e.setFixedSize(519, 227)
e.move(5, 5)

b = QPushButton('1', win)
b.setFont(f)
b.setFixedSize(100, 100)
b.setStyleSheet("background-color:#4259de")
b.move(5, 236)

b1 = QPushButton('2', win)
b1.setFont(f)
b1.setFixedSize(100, 100)
b1.setStyleSheet("background-color:#4259de")
b1.move(110, 236)

b2 = QPushButton('3', win)
b2.setFont(f)
b2.setFixedSize(100, 100)
b2.setStyleSheet("background-color:#4259de")
b2.move(215, 236)

b3 = QPushButton('4', win)
b3.setFont(f)
b3.setFixedSize(100, 100)
b3.setStyleSheet("background-color:#3873e3")
b3.move(5, 341)

b4 = QPushButton('5', win)
b4.setFont(f)
b4.setFixedSize(100, 100)
b4.setStyleSheet("background-color:#3873e3")
b4.move(110, 341)

b5 = QPushButton('6', win)
b5.setFont(f)
b5.setFixedSize(100, 100)
b5.setStyleSheet("background-color:#3873e3")
b5.move(215, 341)

b6 = QPushButton('7', win)
b6.setFont(f)
b6.setFixedSize(100, 100)
b6.setStyleSheet("background-color:#2e8ce8")
b6.move(5, 446)

b7 = QPushButton('8', win)
b7.setFont(f)
b7.setFixedSize(100, 100)
b7.setStyleSheet("background-color:#2e8ce8")
b7.move(110, 446)

b8 = QPushButton('9', win)
b8.setFont(f)
b8.setFixedSize(100, 100)
b8.setStyleSheet("background-color:#2e8ce8")
b8.move(215, 446)

b9 = QPushButton('C', win)
b9.setFont(f)
b9.setFixedSize(100, 100)
b9.setStyleSheet("background-color:red")
b9.move(5, 551)

b0 = QPushButton('0', win)
b0.setFont(f)
b0.setFixedSize(100, 100)
b0.setStyleSheet("background-color:#2999eb")
b0.move(110, 551)

b10 = QPushButton('=', win)
b10.setFont(f)
b10.setFixedSize(310, 100)
b10.setStyleSheet("background-color:#2999eb")
b10.move(215, 551)

b11 = QPushButton('+', win)
b11.setFont(f)
b11.setFixedSize(100, 100)
b11.setStyleSheet("background-color:#0066d6")
b11.move(320, 236)

b12 = QPushButton('-', win)
b12.setFont(f)
b12.setFixedSize(100, 100)
b12.setStyleSheet("background-color:#0066d6")
b12.move(425, 236)

b13 = QPushButton('*', win)
b13.setFont(f)
b13.setFixedSize(100, 100)
b13.setStyleSheet("background-color:#0080cc")
b13.move(320, 341)

b14 = QPushButton('^', win)
b14.setFont(f)
b14.setFixedSize(100, 100)
b14.setStyleSheet("background-color:#0080cc")
b14.move(425, 341)

b15 = QPushButton('/', win)
b15.setFont(f)
b15.setFixedSize(100, 100)
b15.setStyleSheet("background-color:#0099c2")
b15.move(320, 446)

b16 = QPushButton('%', win)
b16.setFont(f)
b16.setFixedSize(100, 100)
b16.setStyleSheet("background-color:#0099c2")
b16.move(425, 446)

def son():
    t = str(int(e.text() + str('1')))
    e.setText(t)

def son0():
    t = str(int(e.text() + str('0')))
    e.setText(t)

def son1():
    t = str(int(e.text() + str('2')))
    e.setText(t)

def son2():
    t = str(int(e.text() + str('3')))
    e.setText(t)

def son3():
    t = str(int(e.text() + str('4')))
    e.setText(t)

def son4():
    t = str(int(e.text() + str('5')))
    e.setText(t)

def son5():
    t = str(int(e.text() + str('6')))
    e.setText(t)

def son6():
    t = str(int(e.text() + str('7')))
    e.setText(t)

def son7():
    t = str(int(e.text() + str('8')))
    e.setText(t)

def son8():
    t = str(int(e.text()+str('9')))
    e.setText(t)

def C():
    global total
    e.setText('0')
    total = ''

def pilus():
    global total
    total = e.text()+'+'
    e.setText('')

def minus():
    global total
    total = e.text()+'-'
    e.setText('')

def kopaytirish():
    global total
    total = e.text()+'*'
    e.setText('')

def daraja():
    global total
    total = e.text()+'**'
    e.setText('')

def bolish():
    global total
    total = e.text()+'/'
    e.setText('')

def qoldiqli_bolish():
    global total
    total = e.text()+'%'
    e.setText('')

def teng():
    global total
    total = total + str(e.text())
    e.setText(str(eval(total)))

b.clicked.connect(son)
b1.clicked.connect(son1)
b2.clicked.connect(son2)
b3.clicked.connect(son3)
b4.clicked.connect(son4)
b5.clicked.connect(son5)
b6.clicked.connect(son6)
b7.clicked.connect(son7)
b8.clicked.connect(son8)
b0.clicked.connect(son0)
b9.clicked.connect(C)
b10.clicked.connect(teng)
b11.clicked.connect(pilus)
b12.clicked.connect(minus)
b13.clicked.connect(kopaytirish)
b14.clicked.connect(daraja)
b15.clicked.connect(bolish)
b16.clicked.connect(qoldiqli_bolish)

win.show()
sys.exit(app.exec_())