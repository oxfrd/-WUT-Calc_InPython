# -*- coding: utf-8 -*-
"""
Created on Thu May 27 18:22:56 2021
@author: oxford
"""
from PyQt5.QtWidgets import QDialog
from sympy.plotting import plot
from PyQt5.uic import loadUi
from time import sleep


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
            p = plot(funkcja, show=False)
            p.save("xy")
            #  sleep(1)

        except TypeError:
            return True
