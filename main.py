from PyQt5.QtWidgets import QApplication
from PyQt5.QtSql import (QSqlDatabase, QSqlQuery)
from _class import mainwindow
from _func import database
import sys



def star():
	app = QApplication(sys.argv)
	app.setStyle('fusion')
	w = mainwindow.MainWindow()
	w.show()
	sys.exit(app.exec_())
if __name__ == '__main__':
	database.newApp()
	star()

