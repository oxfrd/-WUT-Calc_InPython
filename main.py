# -*- coding: utf-8 -*-
"""
Created on Tue May  4 11:30:47 2021

@author: oxford

Calculator app to Python subject on WUT
"""

import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog,QMainWindow, QApplication
from PyQt5.uic import loadUi


class MainWin(QMainWindow):
    def __init__(self):
        super(MainWin, self).__init__()
        loadUi("main_win.ui", self)
        
    def fun_wynikRownania(self):
        funkcja = self.edt_funkcja.text()
        print("Hej: ",funkcja)
        
    def fun_calka(self):
        print("fun calka")

    def fun_pochodna(self):
        print("fun pochodna")

    def fun_wykres(self):
        print("fun wykres")
    
    def fun_mscZerowe(self):
        print("fun zerowe")



class Wyniki(QDialog):
    def __init__(self):
        super(Wyniki, self).__init__()
        loadUi("Wyniki.ui",self)
        
    
app = QApplication(sys.argv)

mainWindow = MainWin()
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainWindow)
widget.show()
app.exec_()
        
        