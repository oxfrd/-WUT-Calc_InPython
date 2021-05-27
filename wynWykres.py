# -*- coding: utf-8 -*-
"""
Created on Thu May 27 18:22:56 2021

@author: oxford
"""
from PyQt5.QtWidgets import QDialog, QWidget
from PyQt5.uic import loadUi
from sympy import symbols
from sympy.plotting import plot


class wynWykres(QDialog):
    def __init__(self):
        super(wynWykres, self).__init__()
        loadUi("wynWykres.ui", self)
        self.Btn_back.clicked.connect(self.hide)

    def rysujWykres(self, funkcja):
        print("Zapisuje wykres")
        try:
            plot(funkcja, show=True)
        except TypeError:
            return True
