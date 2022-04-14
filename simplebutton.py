import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QSize    

class MainWindow(QMainWindow):
    def _init_(self):
        QMainWindow._init_(self)

        self.setMinimumSize(QSize(400, 200))    
        self.setWindowTitle("Button example") 

        pybutton = QPushButton('Login', self)
        pybutton2 = QPushButton('Sign up', self)
        
        pybutton.move(5,5)
        pybutton2.move(50, 50)        

    

if _name_ == "_main_":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit( app.exec_() )
