import sys 

from PyQt5 import QtWidgets  

from PyQt5.QtWidgets import QApplication, QMainWindow 

def window(): 

    app=QApplication(sys.argv) 

    win = QMainWindow() 

    win.setGeometry(100,100,800,800) 

       win.show() 

    sys.exit(app.exec_()) 

window() 
