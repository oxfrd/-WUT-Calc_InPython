# -*- coding: utf-8 -*-
"""
Created on Wed May 26 12:32:26 2021

@author: oxford
"""

from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi

# =============================================================================
# Klasa okna wyniku calkowania
# =============================================================================


class wynPochodna(QDialog):
    """Class of integration result window."""

    def __init__(self):
        """
        Contruct object.

        Returns
        -------
        None.
        """
        super(wynPochodna, self).__init__()
        loadUi("wynPochodna.ui", self)
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

    def tekstPochodnej(self, wynik):
        """
        Put result into window.

        Parameters
        ----------
        wynik : string
            Result of derivative.
        Returns
        -------
        None.
        """
        self.lab_wynPochodna.setText(wynik)
        print("tekst pochodnej")
