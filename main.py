# -*- coding: utf-8 -*-
"""
Created on Tue May  4 11:30:47 2021

@author: oxford

Calculator app to Python subject on WUT
"""

import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QMainWindow, QApplication
from PyQt5.uic import loadUi


class MainWin(QMainWindow):
    def __init__(self):
        super(MainWin, self).__init__()
        loadUi("main_win.ui", self)
        self.setWindowIcon(QIcon('kalkulator.png'))

    def fun_wynikRownania(self):
        funkcja = self.edt_funkcja.text()
        print("Hej: ", funkcja)

    def fun_calka(self):
        print("fun calka")
        funkcja = self.edt_funkcja.text()
        oknoCalki = wynCalka()
        oknoCalki.show()
        oknoCalki.tekstFunkcji(funkcja)

        # widget.addWidget(oknoCalki)
        # widget.setCurrentIndex(widget.currentIndex()+1)

    def fun_pochodna(self):
        print("fun pochodna")

    def fun_wykres(self):
        print("fun wykres")

    def fun_mscZerowe(self):
        print("fun zerowe")


class wynCalka(QDialog):
    def __init__(self):
        super(wynCalka, self).__init__()
        loadUi("wynCalka.ui", self)
        self.Btn_back.clicked.connect(self.hide)

    def tekstFunkcji(self, funkcja):
        self.lab_funkcja.setText(funkcja)
        print("wchodze")
        self.Btn_back.clicked.connect(self.main_window.show)


app = QApplication(sys.argv)
mainWindow = MainWin()
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainWindow)
widget.show()
app.exec_()

# class Manager():
#     def __init__(self):
#         super(Manager, self).__init__()
#         self.main_window = MainWin()
#         self.wynik_calki = wynCalka()

#         self.main_window.Btn_Calka.clicked.connect(self.wynik_calki.show)
#         self.wynik_calki.Btn_back.clicked.connect(self.main_window.show)

#         self.main_window.show()


# app = QApplication(sys.argv)
# manager = Manager()
# sys.exit(app.exec_())
