import sys
import time
import math
from PyQt5 import QtWidgets, QtGui, QtCore, Qt



class OnlyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(OnlyWindow, self).__init__()
        self.setGeometry(50, 50, 450, 400)
        self.setWindowTitle("Typeracer")
        self.setWindowIcon(QtGui.QIcon("icon.ico"))
        f1 = QtGui.QFont()
        l1 = QtWidgets.QLabel(self)
        l1.setText("When life has got you in a slump, turn to these inspirational short stories. \n"
                   "Not only is reading them like getting an internet hug for the soul, \n"
                   "but they just may spark an idea or a change in you for the better. \n"
                   "Read on and get ready to smile.")
        l1.move(10, 10)
        l1.resize(600,200)
        l1.setFont(f1)
        demo = TextEditClass(self)
        demo.move(10,150)
        demo.setStyleSheet("color: rgb(0, 255, 0);")
        demo.resize(430, 200)
        #demo.showdialog(self)




        extractAction = QtWidgets.QAction("&Exit", self)
        extractAction.setShortcut("Ctrl+Q")
        extractAction.setStatusTip('Leave The App')
        extractAction.triggered.connect(self.close_application)

        self.statusBar()

        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('&File')
        fileMenu.addAction(extractAction)

        self.show()



    def close_application(self):
        sys.exit()




class TextEditClass(QtWidgets.QTextEdit):
    def __init__(self, parent):
        super().__init__(parent)

    i=0
    acc = 0


    def keyPressEvent(self, event):
        txt = event.text()

        if(event.key()==QtCore.Qt.Key_Escape or event.key()==QtCore.Qt.Key_Backspace or event.key()==QtCore.Qt.Key_Shift or event.key()==QtCore.Qt.Key_CapsLock):
            pass
        else:
            font = QtGui.QFont()
            line = "When life has got you in a slump, turn to these inspirational short stories. Not only is reading them like getting an internet hug for the soul, but they just may spark an idea or a change in you for the better. Read on and get ready to smile."
            #line = "mynameislol"
            word = line.split()
            lenwords = len(word)
            lenchars = len(line)
            accuracy = (lenchars - self.acc)/lenchars*100
            if (self.i >= len(line)-1):


                final = time.time()
                diff = int(final - self.now)/60
                wpm = (int(lenwords/diff))

                showdialog(wpm, accuracy)




            if (txt == line[self.i]):
                if (txt == ' '):
                    pass
                else:
                    self.insertHtml(
                        '<span style="color: green">'
                        + txt +
                        '</span>')
                    self.i = self.i + 1
                    if(self.i == 1):
                        self.now = time.time()

            else:
                if (txt == ' '):
                    self.acc = self.acc + 1
                else:
                    self.insertHtml(
                        '<span style="color: red">'
                        + txt +
                        '</span>')
                    self.i = self.i + 1
                    if (self.i == 1):
                        self.now = time.time()
                    self.acc = self.acc + 1

            if (txt == ' '):
                self.i = self.i + 1
                if (self.i == 1):
                    self.now = time.time()
                super(TextEditClass, self).keyPressEvent(event)

def msgbtn():
    sys.exit()

def showdialog(wpm, accuracy):
    accuracy = round(accuracy, 2)
    msg = QtWidgets.QMessageBox()
    msg.setIcon(QtWidgets.QMessageBox.Information)
    msg.setWindowIcon(QtGui.QIcon("icon.ico"))
    msg.setText("Words per minute: " + str(wpm))
    msg.setInformativeText("Accuracy: " + str(accuracy))
    msg.setWindowTitle("Typeracer stats")
    msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
    msg.buttonClicked.connect(msgbtn)
    msg.move(100, 100)
    msg.show()
    msg.close(msg.exec_())


app = QtWidgets.QApplication(sys.argv)
window = OnlyWindow()
sys.exit(app.exec_())
