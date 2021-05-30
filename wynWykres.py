# -*- coding: utf-8 -*-
"""
Created on Thu May 27 18:22:56 2021

@author: oxford
"""
from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi
from sympy.plotting import plot


class wynWykres(QDialog):
    """Class of integration result window."""

    def __init__(self):
        """
        Contruct object.

        Returns
        -------
        None.
        """
        super(wynWykres, self).__init__()
        loadUi("wynWykres.ui", self)
        self.Btn_back.clicked.connect(self.hide)

    def rysujWykres(self, funkcja):
        """
        Generate plot of passed function.

        Parameters
        ----------
        funkcja : string
            Function to be plotted.

        Returns
        -------
        bool
            'True' and pop-up -- there is no errors.
            'False' -- there is error.
        """
        print("Zapisuje wykres")
        try:
            plot(funkcja, show=True)
        except TypeError:
            return True
