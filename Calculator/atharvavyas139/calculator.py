'''
Created on 12-Oct-2016

@author: atharvavyas
'''
import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from decimal import Decimal
class Window(QWidget):
    def __init__(self,parent=None):
        QWidget.__init__(self,parent)
        self.grid=QGridLayout()
        self.i1=QLabel("Input1")
        self.i1.setAlignment(Qt.AlignCenter)
        self.i2=QLabel("Input 2")
        self.i2.setAlignment(Qt.AlignCenter)
        self.in1=QLineEdit()
        self.in2=QLineEdit()
        self.in1.setValidator(QDoubleValidator(-100000,100000,4))
        self.in2.setValidator(QDoubleValidator(-100000,100000,4))
        self.grid.addWidget(self.i1,1,1,1,1)
        self.grid.addWidget(self.in1,1,2,1,3)
        self.grid.addWidget(self.i2,2,1,1,1)
        self.grid.addWidget(self.in2,2,2,1,3)
        self.b1=QPushButton("+")
        self.b1.clicked.connect(self.cfunction)
        self.b2=QPushButton("-")
        self.b2.clicked.connect(self.cfunction)
        self.b3=QPushButton("*")
        self.b3.clicked.connect(self.cfunction)
        self.b4=QPushButton("/")
        self.b4.clicked.connect(self.cfunction)
        self.b5=QPushButton("HCF")
        self.b5.clicked.connect(self.cfunction)
        self.b6=QPushButton("LCM")
        self.b6.clicked.connect(self.cfunction)
        self.grid.addWidget(self.b1,3,1)
        self.grid.addWidget(self.b2,3,2)
        self.grid.addWidget(self.b3,3,3)
        self.grid.addWidget(self.b4,3,4)
        self.grid.addWidget(self.b5,4,1,1,2)
        self.grid.addWidget(self.b6,4,3,1,2)
        self.i3=QLabel("Answer:")
        self.i3.setAlignment(Qt.AlignCenter)
        self.ans=QLineEdit();
        self.grid.addWidget(self.i3,5,1,1,1)
        self.grid.addWidget(self.ans,5,2,1,3)
        self.setLayout(self.grid)
        self.setGeometry(400,400,600,400)
        self.setWindowTitle("Calculator")
        self.icon=QIcon("favicon.ico")
        self.setWindowIcon(self.icon)
    def cfunction(self):
        x=self.sender()
        a=float(self.in1.text())
        b=float(self.in2.text())
        if x.text()=="+":
            self.ans.setText(str(a+b))
        elif x.text()=="-":
            self.ans.setText(str(a-b))
        elif x.text()=="*":
            self.ans.setText(str(a*b))
        elif x.text()=="/":
            self.ans.setText(str(a/b))
        elif x.text()=="HCF":
            self.ans.setText(str(self.hcf(a,b)))
        elif x.text()=="LCM":
            self.ans.setText(str(self.lcm(a,b)))
    def hcf(self,a,b):
        if b==0:
            return a
        return self.hcf(b,a%b)
    def lcm(self,a,b):
        return (a*b)/(self.hcf(a,b))
def perform():
    app=QApplication(sys.argv)
    window=Window()
    window.show()
    sys.exit(app.exec())
if __name__=="__main__":
    perform()