#-*-coding:utf-8-*-
from PyQt4.QtGui import *
from PyQt4 import uic


class AnaPencere(QMainWindow):
	def __init__(self,ebeveyn=None):
		QWidget.__init__(self,ebeveyn)
		self.ui = uic.loadUi('qt1.ui',self)
	

uygulama = QApplication([])
pencere = AnaPencere()
pencere.show()
uygulama.exec_()
