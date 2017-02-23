import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from random import randint
import time
from io import *
def required_string():
    f=open("test.txt","r+")
    s=f.read()
    l=[]
    l=s.split("-")
    x=randint(0,len(l)-1)
    return l[x]
class Window(QWidget):
    def __init__(self,parent=None):
        QWidget.__init__(self,parent)
        self.lt=QGridLayout()
        self.l1=QLabel("")
        self.pallet=QPalette()
        self.s=required_string()
        self.l1list=[]
        self.l1list=self.s.split()
        self.l1.setText(self.s)
        self.inp=QLineEdit("")
        self.countw=0
        self.countcw=0
        self.start=time.time()
        self.pallet.setColor(QPalette.Foreground,Qt.green)
        self.l1.setPalette(self.pallet)
        self.inp.textChanged.connect(self.textchanged)
        self.b1=QPushButton("Change paragraph")
        self.b1.clicked.connect(self.pressed)
        self.l2=QLabel("WPM:")
        self.op=QLineEdit("")
        self.lt.addWidget(self.l1,1,1,4,4)
        self.lt.addWidget(self.inp,5,1,4,4)
        self.lt.addWidget(self.l2,9,1,1,1)
        self.lt.addWidget(self.op,9,2,1,1)
        self.lt.addWidget(self.b1,9,4,1,1)
        self.setLayout(self.lt)
    def textchanged(self):
        self.t=self.inp.text()
        self.diff=(time.time()-self.start)
        print(self.l1list[self.countw])
        print(self.t)
        if(self.t==self.l1list[self.countw]):
            self.optextchange(1)
        elif len(self.t)>1:
            self.a=len(self.t)
            if self.t[len(self.t)-1]=='\n' or self.t[len(self.t)-1]==' ':
                self.countw=self.countw+1
                self.inp.setText("")
                self.optextchange(0)
    def optextchange(self,a):
        if a==1:
            self.countcw=self.countcw+1
            self.op.setText(str(self.countcw*60/self.diff))
    def pressed(self):
        self.s=required_string()
        self.l1list=[]
        self.l1list=self.s.split()
        self.l1.setText(self.s)
        self.start=time.time()
        self.countcw=0
        self.countw=0
def perform():
    app=QApplication(sys.argv)
    window=Window()
    window.show()
    sys.exit(app.exec())
if __name__=="__main__":
    perform()
    