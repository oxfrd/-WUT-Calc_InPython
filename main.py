# -*- coding: utf-8 -*-
"""
Created on Tue May  4 11:30:47 2021

@author: oxford

Calculator app to Python subject on WUT
"""

import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.uic import loadUi
from PyQt5.QtGui import QIcon


from errorshandling import bledy
from core import obliczenia
from wynCalka import wynCalka
from wynPochodna import wynPochodna
from wynZero import wynZero

# =============================================================================
# Klasa okna wyniku calkowania
# =============================================================================


class MainWin(QMainWindow):
    def __init__(self):
        super(MainWin, self).__init__()
        loadUi("main_win.ui", self)
        self.setWindowIcon(QIcon('ikona.png'))

    def fun_calka(self):
        print("fun calka")
        funkcja = self.edt_funkcja.text()
        po = self.edt_funkcjaPo.text()
        od = self.edt_od.text()
        do = self.edt_do.text()
        czyOznaczona = False

        if self.cbox_ozn.isChecked():
            czyOznaczona = True
            przerwij = bledy.sprawdzOdDO(self, od, do)
            print("oznaczona")
            if przerwij is False:
                return

        przerwij = bledy.PoprawneDaneIntDif(self, funkcja, po)

        if przerwij is False:
            return

        oknoCalki = wynCalka()

        oknoCalki.tekstFunkcji(funkcja)
        if czyOznaczona:
            wynik = obliczenia.calkowanieOzn(funkcja, po, od, do)
        else:
            wynik = obliczenia.calkowanie(funkcja, po)
        oknoCalki.tekstCalki(wynik)
        oknoCalki.show()
        oknoCalki.exec_()

    def fun_pochodna(self):
        print("fun pochodna")
        funkcja = self.edt_funkcja.text()
        po = self.edt_funkcjaPo.text()

        przerwij = bledy.PoprawneDaneIntDif(self, funkcja, po)

        if przerwij is False:
            return

        oknoPochodnej = wynPochodna()
        oknoPochodnej.tekstFunkcji(funkcja)
        wynik = obliczenia.pochodna(funkcja, po)
        oknoPochodnej.tekstPochodnej(wynik)
        oknoPochodnej.show()
        oknoPochodnej.exec_()

    def fun_mscZerowe(self):
        print("fun zerowe")
        funkcja = self.edt_funkcja.text()
        przerwij = bledy.PoprawneDaneRow(self, funkcja)

        if przerwij is False:
            return
        
        oknoZer = wynZero()
        oknoZer.tekstFunkcji(funkcja)
        wynik = obliczenia.MiejsceZerowe(funkcja)
        oknoZer.tekstWynik(wynik)
        oknoZer.show()
        oknoZer.exec_()
        
    def fun_wykres(self):
        print("fun wykres")



# =============================================================================
# End of classes
# =============================================================================


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
