# importing the required libraries

from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5.QtGui import *
import sys


class Window(QMainWindow):
	def _init_(self):
		super()._init_()

		# changing the background color to yellow
		self.setStyleSheet("background-color: yellow;")

		# set the title
		self.setWindowTitle("Color")

		# setting the geometry of window
		self.setGeometry(0, 0, 400, 300)

		# show all the widgets
		self.show()


# create pyqt5 app
App = QApplication(sys.argv)

# create the instance of our Window
window = Window()

# start the app
sys.exit(App.exec())
