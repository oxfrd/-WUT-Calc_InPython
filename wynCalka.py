# -*- coding: utf-8 -*-
"""
Created on Wed May 26 11:44:16 2021

@author: oxford
"""

from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi

# =============================================================================
# Klasa okna wyniku calkowania
# =============================================================================


class wynCalka(QDialog):
    """Class of integration result window."""

    def __init__(self):
        """
        Contruct object.

        Returns
        -------
        None.
        """
        super(wynCalka, self).__init__()
        loadUi("wynCalka.ui", self)
        self.Btn_back.clicked.connect(self.hide)

    def tekstFunkcji(self, funkcja):
        """
        Put calculated function into window.

        Parameters
        ----------
        wynik : string
            Result of integration.
        Returns
        -------
        None.
        """
        self.lab_funkcja.setText(funkcja)
        print("tekst funkcji")

    def tekstCalki(self, wynik):
        """
        Put result into window.

        Parameters
        ----------
        wynik : string
            Result of integration.
        Returns
        -------
        None.
        """
        self.lab_wynCalka.setText(wynik)
        print("tekst calki")
