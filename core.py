# -*- coding: utf-8 -*-
"""
Created on Mon May 24 20:20:31 2021

@author: oxford
"""
from sympy import *


class obliczenia():

    def calkowanie(Funkcja, PoCzym):
        init_printing(use_unicode=False, wrap_line=False)
        if PoCzym == 'x':
            x = symbols('x')
            wynik = integrate(Funkcja, x)
        if PoCzym == 'y':
            y = symbols('y')
            wynik = integrate(Funkcja, y)
        if PoCzym == 'z':
            z = symbols('z')
            wynik = integrate(Funkcja, z)
            
        print(wynik)
        string = str(wynik)
        print(string)
        return string
