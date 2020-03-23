# Windows -> QT Designer, if you don't have it, install it
# import PyQt5 sa shown to bind it
# https://build-system.fman.io/qt-designer-download
# QMessageBox

# pyuic5 -x dialog.ui -o test.py

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

class MyWindow(QMainWindow):  # Essentially just changing the name of the class by inheriting
    def __init__(self):
        super(MyWindow, self).__init__()  # Used to inherit the init used for the normal QMainWindow class
        self.setGeometry(200, 200, 300, 300)
        self.setWindowTitle("QT Tutorial")
        self.initUI()

    def initUI(self):   # All the stuff on this screen in here
        self.label = QtWidgets.QLabel(self)
        self.label.setText("My first label")
        self.label.move(50, 50)

        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText("click me")
        self.b1.clicked.connect(self.clicked)

    def clicked(self):
        self.label.setText("You pressed the button")
        self.update()

    def update(self):
        self.label.adjustSize()

def clicked():
    print("clicked")

def window():
    app = QApplication(sys.argv) # Gives config setup for operation dependent on the system OS
    win = MyWindow()
    win.show()  # Shows the window
    sys.exit(app.exec_())  # Exits properly upon clicking exit

window()


# Form, Window = uic.loadUiType("dialog.ui")
#
# app = QApplication([])
# window = Window()
# form = Form()
# form.setupUi(window)
# window.show()
# app.exec_()

