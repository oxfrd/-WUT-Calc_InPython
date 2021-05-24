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
