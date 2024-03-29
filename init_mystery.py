# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/Artem/Desktop/АРТЕМ/ELGames/QT_mystery.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from resurse_lib import Resurse


class Ui_mystery(object):
	def setupUi(self, mystery):
		mystery.setObjectName("mystery")
		mystery.resize(666, 394)
		with open(Resurse("theme").read(), "r") as file:
			text = file.read()
			mystery.setStyleSheet(text)
		self.bals = QtWidgets.QLabel(mystery)
		self.bals.setGeometry(QtCore.QRect(530, 50, 121, 31))
		self.bals.setStyleSheet("font: 75 14pt \"Verdana\";\n"
								"background-color: none;\nborder: none;")
		self.bals.setAlignment(QtCore.Qt.AlignLeading |
							   QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
		self.bals.setObjectName("bals")
		self.heart = QtWidgets.QLabel(mystery)
		self.heart.setGeometry(QtCore.QRect(490, 50, 31, 31))
		self.heart.setStyleSheet("background-color: none;\nborder: none;")
		self.heart.setText("")
		self.heart.setPixmap(QtGui.QPixmap(Resurse("heart").read()))
		self.heart.setScaledContents(True)
		self.heart.setObjectName("heart")
		self.icon_2 = QtWidgets.QLabel(mystery)
		self.icon_2.setGeometry(QtCore.QRect(10, 10, 61, 61))
		self.icon_2.setStyleSheet("background-color: none;\nborder: none;")
		self.icon_2.setText("")
		self.icon_2.setPixmap(QtGui.QPixmap(Resurse("option").read()))
		self.icon_2.setScaledContents(True)
		self.icon_2.setWordWrap(False)
		self.icon_2.setOpenExternalLinks(False)
		self.icon_2.setObjectName("icon_2")
		self.pushButton = QtWidgets.QPushButton(mystery)
		self.pushButton.setGeometry(QtCore.QRect(10, 10, 61, 61))
		self.pushButton.setStyleSheet("background-color: none;\nborder: none")
		self.pushButton.setText("")
		self.pushButton.setObjectName("pushButton")
		self.home = QtWidgets.QPushButton(mystery)
		self.home.setGeometry(QtCore.QRect(560, 350, 91, 31))
		self.home.setObjectName("home")
		self.reb = QtWidgets.QLabel(mystery)
		self.reb.setGeometry(QtCore.QRect(150, 40, 331, 161))
		self.reb.setText("")
		self.reb.setScaledContents(True)
		self.reb.setWordWrap(True)
		self.reb.setObjectName("reb")
		self.otvet = QtWidgets.QLineEdit(mystery)
		self.otvet.setGeometry(QtCore.QRect(150, 260, 331, 51))
		self.otvet.setStyleSheet("")
		self.otvet.setAlignment(QtCore.Qt.AlignCenter)
		self.otvet.setObjectName("otvet")
		self.ask = QtWidgets.QPushButton(mystery)
		self.ask.setGeometry(QtCore.QRect(150, 320, 331, 31))
		self.ask.setStyleSheet("")
		self.ask.setObjectName("ask")
		self.lol = QtWidgets.QPushButton(mystery)
		self.lol.setGeometry(QtCore.QRect(490, 260, 141, 51))
		self.lol.setObjectName("lol")
		self.label = QtWidgets.QLabel(mystery)
		self.label.setGeometry(QtCore.QRect(200, 210, 231, 41))
		self.label.setAlignment(QtCore.Qt.AlignCenter)
		self.label.setObjectName("label")
		self.svaip = QtWidgets.QPushButton(mystery)
		self.svaip.setGeometry(QtCore.QRect(490, 210, 141, 41))
		self.svaip.setObjectName("svaip")
		self.green = QtWidgets.QLabel(mystery)
		self.green.setGeometry(QtCore.QRect(150, 210, 41, 41))
		self.green.setText("")
		self.green.setPixmap(QtGui.QPixmap("Ресурс/green_reb.png"))
		self.green.setObjectName("green")
		self.red1 = QtWidgets.QLabel(mystery)
		self.red1.setGeometry(QtCore.QRect(150, 210, 41, 41))
		self.red1.setText("")
		self.red1.setPixmap(QtGui.QPixmap("Ресурс/red_reb.jpg"))
		self.red1.setObjectName("red1")
		self.red = QtWidgets.QLabel(mystery)
		self.red.setGeometry(QtCore.QRect(440, 210, 41, 41))
		self.red.setText("")
		self.red.setPixmap(QtGui.QPixmap("Ресурс/red_reb.jpg"))
		self.red.setObjectName("red")
		self.green1 = QtWidgets.QLabel(mystery)
		self.green1.setGeometry(QtCore.QRect(440, 210, 41, 41))
		self.green1.setText("")
		self.green1.setPixmap(QtGui.QPixmap("Ресурс/green_reb.png"))
		self.green1.setObjectName("green1")
		self.green.setVisible(False)
		self.red.setVisible(False)
		self.green1.setVisible(False)
		self.red1.setVisible(False)
		self.retranslateUi(mystery)
		QtCore.QMetaObject.connectSlotsByName(mystery)

	def retranslateUi(self, mystery):
		_translate = QtCore.QCoreApplication.translate
		mystery.setWindowTitle(_translate("mystery", "Form"))
		self.bals.setText(_translate("mystery", "<html><head/><body><p>0</p></body></html>"))
		self.home.setText(_translate("mystery", "назад"))
		self.ask.setText(_translate("mystery", "ОТВЕТИТЬ!"))
		self.lol.setText(_translate("mystery", "Показать ответ"))
		self.label.setText(_translate("mystery", "↓ Напиши слово ↓"))
		self.svaip.setText(_translate("mystery", "Пропустить"))


if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	mystery = QtWidgets.QWidget()
	ui = Ui_mystery()
	ui.setupUi(mystery)
	mystery.show()
	sys.exit(app.exec_())
