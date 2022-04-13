# importing the required libraries  

import sys 

from PyQt5 import QtCore, QtWidgets 

from PyQt5.QtWidgets import QMainWindow, QLabel, QCheckBox, QWidget, QApplication 

from PyQt5.QtCore import QSize  

class Window(QMainWindow):  

    def __init__(self):  

        super().__init__()  

        # set the title  

        self.setWindowTitle("checkbox")  

        # setting  the geometry of window  

        self.setGeometry(200, 200, 600, 600)  

        self.b = QCheckBox("Awesome?",self) 

        self.b.stateChanged.connect(self.clickBox) 

        self.b.move(20,20) 

        self.b.resize(320,40) 

 
 

    def clickBox(self, state): 

 
 

        if state == QtCore.Qt.Checked: 

            print('Checked') 

        else: 

            print('Unchecked') 

 
 

        self.show()  

# create pyqt5 app  

App = QApplication(sys.argv)  

# create the instance of our Window  

window = Window()  

# start the app  

sys.exit(App.exec()) 
