import sys 

from PyQt5.QtWidgets import QApplication, QWidget 

from PyQt5.QtGui import QIcon 

class App(QWidget): 

      def __init__(self): 

              super().__init__() 

              self.initUI() 

      def initUI(self): 

              self.setWindowTitle('Hello, world!') 

              self.setGeometry(200,200,500,500) 

              self.show() 

if __name__=='__main__': 

        app=QApplication(sys.argv) 

        ex=App() 

        sys.exit(app.exec_()) 
