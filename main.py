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
from sympy.plotting import plot

from errorshandling import bledy
from core import obliczenia
from wynCalka import wynCalka
from wynPochodna import wynPochodna
from wynZero import wynZero
from wynWykres import wynWykres


# =============================================================================
# Klasa glownego okna
# =============================================================================


class MainWin(QMainWindow):
    """
    Class of main window.

    This class is handling main window of application functions
    after clicking of any buttons.
    """

    def __init__(self):
        """Constructo of class MainWin."""
        super(MainWin, self).__init__()
        loadUi('main_win.ui', self)

    def fun_calka(self):
        """
        Dialog window with integrating result.

        Fun is being called when Btn_calka is clicked.
        It takes function from edt_funkcja, give it to core,
        checking if it's definite integrate. Depends on that
        chose calculating function and print result.

        Returns
        -------
        None.

        """
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

        if wynik is False:
            bledy.zlaFunkcja(self)
            return

        oknoCalki.tekstCalki(wynik)
        oknoCalki.show()
        oknoCalki.exec_()

    def fun_pochodna(self):
        """
        Dialog window with derivative result.

        Function is being called when Btn_pochodna is clicked.
        It takes function from edt_funkcja, give it to core
        to calculating function and print result.

        Returns
        -------
        None.

        """
        print("fun pochodna")
        funkcja = self.edt_funkcja.text()
        po = self.edt_funkcjaPo.text()

        przerwij = bledy.PoprawneDaneIntDif(self, funkcja, po)

        if przerwij is False:
            return

        oknoPochodnej = wynPochodna()
        oknoPochodnej.tekstFunkcji(funkcja)
        wynik = obliczenia.pochodna(funkcja, po)
        if wynik is False:
            bledy.zlaFunkcja(self)
            return

        oknoPochodnej.tekstPochodnej(wynik)
        oknoPochodnej.show()
        oknoPochodnej.exec_()

    def fun_mscZerowe(self):
        """
        Dialog window with zero points result.

        Function is being called when Btn_MiejscaZerowe
        is clicked. It takes function from edt_funkcja,
        give it to core to calculating function and
        print result.

        Returns
        -------
        None.

        """
        print("fun zerowe")
        funkcja = self.edt_funkcja.text()
        przerwij = bledy.PoprawneDaneRow(self, funkcja)

        if przerwij is False:
            return

        oknoZer = wynZero()
        oknoZer.tekstFunkcji(funkcja)
        wynik = obliczenia.MiejsceZerowe(funkcja)

        if wynik is False:
            bledy.zlaFunkcja(self)
            return

        oknoZer.tekstWynik(wynik)
        oknoZer.show()
        oknoZer.exec_()

    def fun_wykres(self):
        """
        Generate plot.

        Function is being called when Btn_Wykres
        is clicked. It takes function from edt_funkcja,
        give it to core to calculating function and
        print result.

        Returns
        -------
        None.
        """
        print("fun wykres")
        funkcja = self.edt_funkcja.text()
        przerwij = bledy.PoprawneDaneRow(self, funkcja)

        if przerwij is False:
            return

        if wynWykres.rysujWykres(self, funkcja) is True:
            bledy.bladWykresu(self)
            return
        wykresOkno = wynWykres()
        wykresOkno.show()
        wykresOkno.exec_()
        return

# =============================================================================
# End of classes
# =============================================================================


app = QApplication(sys.argv)
mainWindow = MainWin()
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainWindow)
widget.show()
app.exec_()
