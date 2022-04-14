# importing the required libraries

from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
import sys


class Window(QMainWindow):
	def _init_(self):
		super()._init_()

		self.acceptDrops()
		# set the title
		self.setWindowTitle("Image")

		# setting the geometry of window
		self.setGeometry(0, 0, 500, 500)

		# creating label
		self.label = QLabel(self)
		
		# loading image
		self.pixmap = QPixmap('Pink_Flower.png')

		# adding image to label
		self.label.setPixmap(self.pixmap)

		# Optional, resize label to image size
		self.label.resize(self.pixmap.width(),
						self.pixmap.height())

		# show all the widgets
		self.show()

# create pyqt5 app
App = QApplication(sys.argv)

# create the instance of our Window
window = Window()

# start the app
sys.exit(App.exec())
