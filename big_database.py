from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QTextEdit, QPushButton, QFileDialog
from PyQt5 import uic
from PyQt5.QtGui import QPixmap
import sys

class UI(QMainWindow):

	def clicker(self):
		fname = QFileDialog.getOpenFileName(self, "Open File", "C:\\Users\\Lali\\Desktop\\--VIPIN--\\Anime\\anime\\Wallpaper (Vipin)", "All Files (*)")

		#Open the image, then add it to the label
		self.pixmap = QPixmap(fname[0])
		self.label.setPixmap(self.pixmap)



	def __init__(self):
		super(UI, self).__init__()
		uic.loadUi("image.ui" , self)


		self.button = self.findChild(QPushButton, "pushButton")
		self.label  = self.findChild(QLabel, "label")


		self.button.clicked.connect(self.clicker)



		self.show()


app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()