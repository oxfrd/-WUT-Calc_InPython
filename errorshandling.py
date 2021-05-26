# -*- coding: utf-8 -*-
"""
Created on Mon May 24 20:58:37 2021

@author: oxford
"""
from PyQt5.QtWidgets import QMessageBox

# =============================================================================
# Klasa obslugi bledow
# =============================================================================


class bledy():

    def __init__(self):
        super(bledy, self).__init__()

    def PoprawneDaneIntDif(self, fun, poCzym):

        if bledy.brakFunkcji(self, fun) is False:
            return False

        if bledy.brakWarunku(self, poCzym) is False:
            return False

        if bledy.zlyWarunek(self, poCzym) is False:
            return False

        return True

    def PoprawneDaneRow(self, fun):

        if bledy.brakFunkcji(self, fun) is False:
            return False
        return True

    def brakFunkcji(self, tekst):
        if len(tekst) == 0:
            QMessageBox.critical(self, 'Błąd',
                                 "Wprowadź poprawną funkcję!")
            return False
        return True

    def brakWarunku(self, tekst):
        if len(tekst) == 0:
            QMessageBox.critical(self, 'Błąd',
                                 "Wprowadź zmienną!")
            return False
        return True

    def zlyWarunek(self, tekst):
        if tekst != 'x' and tekst != 'y' and tekst != 'z':
            QMessageBox.critical(self, 'Błąd',
                                 "Wprowadź poprawną zmienną (x, y lub z)!")

            return False
        return True

    def sprawdzOdDO(self, tekst, tekst2):
        exception = False
        try:
            od = int(tekst)
        except ValueError:
            try:
                od = float(tekst)
            except ValueError:
                if tekst.find('pi') > -1 or tekst.find('sqrt') > -1 or tekst.find('log') > -1 or tekst.find('ln') > -1 or tekst.find('sin') > -1 or tekst.find("cos") > -1 or tekst.find('tan') > -1 or tekst.find('ctan') > -1:
                    exception = True
                else:
                    QMessageBox.critical(self, 'Błąd! [1]',
                                         "Wprowadź poprawne warunki brzegowe!")
                    return False
            else:
                pass
        else:
            pass

        try:
            do = int(tekst2)
        except ValueError:
            try:
                do = float(tekst2)
            except ValueError:
                if tekst.find('pi') > -1 or tekst.find('sqrt') > -1 or tekst.find('log') > -1 or tekst.find('ln') > -1 or tekst.find('sin') > -1 or tekst.find("cos") > -1 or tekst.find('tan') > -1 or tekst.find('ctan') > -1:
                    exception = True
                else:
                    QMessageBox.critical(self, 'Błąd! [1]',
                                         "Wprowadź poprawne warunki brzegowe!")
                    return False
            else:
                pass
        else:
            pass

        if len(tekst) == 0 or len(tekst2) == 0:

            QMessageBox.critical(self, 'Błąd! [3]',
                                 "Wprowadź poprawne warunki brzegowe!")
            return False

        if (exception is False) and (od > do):

            QMessageBox.critical(self, 'Błąd! [4]',
                                 "Wartosć 'od' jest większa niż 'do'. Zweryfikuj dane warunki brzegowe")
            return False
