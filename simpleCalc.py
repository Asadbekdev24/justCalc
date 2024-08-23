
from PyQt5.QtWidgets import QApplication, QWidget,QLabel, QPushButton,QLineEdit

from PyQt5.QtGui import QIcon
import os
os.system("cls")

app=QApplication([])

oyna=QWidget()
oyna.setWindowTitle("Just calc")
oyna.setWindowIcon(QIcon("images.jpg"))

oyna.setGeometry(700,150,600,800)
oyna.setStyleSheet("""
background-color:#E0F7FA;
""")

inputNum=QLineEdit(oyna)
inputNum.setPlaceholderText("Son kiriting")
inputNum.setGeometry(145,100,280,50)
inputNum.setStyleSheet("""
border-radius:5px;
font-size:20px;
border:2px solid green;
""")

btn1=QPushButton("1",oyna)
btn1.setGeometry(150,180,50,50)
btn1.setStyleSheet("""
border-radius:20px;
font-size:20px;
border:2px solid green;
""")

btn2=QPushButton("2",oyna)
btn2.setGeometry(220,180,50,50)
btn2.setStyleSheet("""
border-radius:20px;
font-size:20px;
border:2px solid green;
""")
btn3=QPushButton("3",oyna)
btn3.setGeometry(290,180,50,50)
btn3.setStyleSheet("""
border-radius:20px;
font-size:20px;
border:2px solid green;
""")

amal1=QPushButton("+",oyna)
amal1.setGeometry(360,180,50,50)
amal1.setStyleSheet("""
border-radius:5px;
font-size:20px;
border:2px solid green;
""")

btn4=QPushButton("4",oyna)
btn4.setGeometry(150,250,50,50)
btn4.setStyleSheet("""
border-radius:20px;
font-size:20px;
border:2px solid green;
""")

btn5=QPushButton("5",oyna)
btn5.setGeometry(220,250,50,50)
btn5.setStyleSheet("""
border-radius:20px;
font-size:20px;
border:2px solid green;
""")
btn6=QPushButton("6",oyna)
btn6.setGeometry(290,250,50,50)
btn6.setStyleSheet("""
border-radius:20px;
font-size:20px;
border:2px solid green;
""")

amal2=QPushButton("-",oyna)
amal2.setGeometry(360,250,50,50)
amal2.setStyleSheet("""
border-radius:5px;
font-size:20px;
border:2px solid green;
""")

btn7=QPushButton("7",oyna)
btn7.setGeometry(150,320,50,50)
btn7.setStyleSheet("""
border-radius:20px;
font-size:20px;
border:2px solid green;
""")

btn8=QPushButton("8",oyna)
btn8.setGeometry(220,320,50,50)
btn8.setStyleSheet("""
border-radius:20px;
font-size:20px;
border:2px solid green;
""")
btn9=QPushButton("9",oyna)
btn9.setGeometry(290,320,50,50)
btn9.setStyleSheet("""
border-radius:20px;
font-size:20px;
border:2px solid green;
""")
amal3=QPushButton("*",oyna)
amal3.setGeometry(360,320,50,50)
amal3.setStyleSheet("""
border-radius:5px;
font-size:20px;
border:2px solid green;
""")
btn0=QPushButton("0",oyna)
btn0.setGeometry(150,390,50,50)
btn0.setStyleSheet("""
border-radius:20px;
font-size:20px;
border:2px solid green;
""")

tengAmali=QPushButton("=",oyna)
tengAmali.setGeometry(220,390,120,50)
tengAmali.setStyleSheet("""
border-radius:5px;
font-size:20px;
border:2px solid green;
""")
amal4=QPushButton("/",oyna)
amal4.setGeometry(360,390,50,50)
amal4.setStyleSheet("""
border-radius:5px;
font-size:20px;
border:2px solid green;
""")

def bir():
    son=inputNum.text()+"1"
    inputNum.setText(son)
def ikki():
    son=inputNum.text()+"2"
    inputNum.setText(son)
def uch():
    son=inputNum.text()+"3"
    inputNum.setText(son)
def tort():
    son=inputNum.text()+"4"
    inputNum.setText(son)
def besh():
    son=inputNum.text()+"5"
    inputNum.setText(son)
def olti():
    son=inputNum.text()+"6"
    inputNum.setText(son)
def yetti():
    son=inputNum.text()+"7"
    inputNum.setText(son)
def sakkiz():
    son=inputNum.text()+"8"
    inputNum.setText(son)
def toqqiz():
    son=inputNum.text()+"9"
    inputNum.setText(son)
def nol():
    son=inputNum.text()+"0"
    inputNum.setText(son)

def plus():
    son=inputNum.text()
    if son[-1]=="+":
        return
    if son[-1] in ["-","/","*"]:
        son=son[:-1]
    inputNum.setText(son+"+")
def minus():
    son=inputNum.text()
    if son[-1]=="-":
        return
    if son[-1] in ["+","/","*"]:
        son=son[:-1]
    inputNum.setText(son+"-")
def kopaytirish():
    son=inputNum.text()
    if son[-1]=="*":
        return
    if son[-1] in ["+","/","-"]:
        son=son[:-1]
    inputNum.setText(son+"*")
def bolish():
    son=inputNum.text()
    if son[-1]=="/":
        return
    if son[-1] in ["+","-","*"]:
        son=son[:-1]
    inputNum.setText(son+"/")

def teng():
    ifoda=inputNum.text()
    if ifoda[-1]=="0":
        inputNum.setText("0 ga bo'lish mumkin emas")
        inputNum.clear()
    else:
        inputNum.setText(str(eval(ifoda)))




btn0.clicked.connect(nol)
btn1.clicked.connect(bir)
btn2.clicked.connect(ikki)
btn3.clicked.connect(uch)
btn4.clicked.connect(tort)
btn5.clicked.connect(besh)
btn6.clicked.connect(olti)
btn7.clicked.connect(yetti)
btn8.clicked.connect(sakkiz)
btn9.clicked.connect(toqqiz)

#amallar
amal1.clicked.connect(plus)
amal2.clicked.connect(minus)
amal3.clicked.connect(kopaytirish)
amal4.clicked.connect(bolish)
tengAmali.clicked.connect(teng)

oyna.show()
app.exec()