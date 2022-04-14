# importing libraries 

from PyQt5.QtWidgets import * 

from PyQt5.QtGui import * 

from PyQt5.QtCore import * 

import sys 

 
 
 

class Window(QMainWindow): 

    def _init_(self): 

        super()._init_() 

 
 

        # setting title 

        self.setWindowTitle("Python ") 

 
 

        # setting geometry 

        self.setGeometry(100, 300, 500, 300) 

 
 

        # calling method 

        self.UiComponents() 

 
 

        # showing all the widgets 

        self.show() 

 
 

    # method for widgets 

    def UiComponents(self): 

 
 

        # creating a push button 

        button = QPushButton("SUBMIT", self) 

 
 

        # setting geometry of button 

        button.setGeometry(200, 150, 100, 30) 

 
 

        # adding action to a button 

        button.clicked.connect(self.clickme) 

 
 

    # action method 

    def clickme(self): 

 
 

        # printing pressed 

        print("You Submited Successfully!!") 

 
 

# create pyqt5 app 

App = QApplication(sys.argv) 

 
 

# create the instance of our Window 

window = Window() 

 
 

# start the app 

sys.exit(App.exec())
