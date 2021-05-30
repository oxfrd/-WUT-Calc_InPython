# -*- coding: utf-8 -*-
"""
Created on Wed May 26 19:21:31 2021

@author: oxford
"""

from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi


class wynZero(QDialog):
    """Class of integration result window."""

    def __init__(self):
        """
        Contruct object.

        Returns
        -------
        None.
        """
        super(wynZero, self).__init__()
        loadUi("wynMiejscaZerowe.ui", self)
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

    def tekstWynik(self, wynik):
        """
        Put result into window.

        Parameters
        ----------
        wynik : string
            Result of calculating.
        Returns
        -------
        None.
        """
        self.lab_wynZerowe.setText(wynik)
        print("tekst zerowej")
