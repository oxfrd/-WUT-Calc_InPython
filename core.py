# -*- coding: utf-8 -*-
"""
Created on Mon May 24 20:20:31 2021

@author: oxford
"""
from sympy import symbols, diff, integrate, solve, Function
f = Function('f')


class obliczenia():
    """
    Class of calculating.

    This class is handling calculations based on sympy
    library.
    """

    def calkowanie(Funkcja, PoCzym):
        """
        Indefinite itegral of passed function.

        Parameters
        ----------
        Funkcja : string
            Function to be integrated.
        PoCzym : string
            Integration variable.

        Returns
        -------
        bool -- "False" if integration return error.
        string -- result of operation if there is not error.
        """
        try:
            if PoCzym == 'x':
                x = symbols('x')
                wynik = integrate(Funkcja, x)
            if PoCzym == 'y':
                y = symbols('y')
                wynik = integrate(Funkcja, y)
            if PoCzym == 'z':
                z = symbols('z')
                wynik = integrate(Funkcja, z)
        except TypeError:
            return False
        else:
            print(wynik)
            string = str(wynik)
            print(string)
            if string.find('Integral') > -1:
                return False
            return string

    def calkowanieOzn(Funkcja, PoCzym, od, do):
        """
        Definite integral of passed function.

        Parameters
        ----------
        Funkcja : string
            Function to be integrated.
        PoCzym : string
            Integration variable.
        od : string
            Integrating from 'od'
        do : string
            Integration to 'do'.

        Returns
        -------
        bool -- "False" if 'integration' return error.
        string -- result of operation if there is not error.
        """
        try:
            if PoCzym == 'x':
                x = symbols('x')
                wynik = integrate(Funkcja, (x, od, do))
                if PoCzym == 'y':
                    y = symbols('y')
                    wynik = integrate(Funkcja, (y, od, do))
                    if PoCzym == 'z':
                        z = symbols('z')
                        wynik = integrate(Funkcja, (z, od, do))
        except TypeError:
            return False
        else:
            print(wynik)
            string = str(wynik)
            print(string)
            if string.find('Integral') > -1:
                return False
            return string

    def pochodna(Funkcja, PoCzym):
        """
        Diffrentiate of passed function.

        Parameters
        ----------
        Funkcja : string
            Function to be diffrentiated.
        PoCzym : string
            Deffretiation variable.

        Returns
        -------
        bool -- "False" if 'diff' return error.
        string -- result of operation if there is not error.
        """
        try:
            if PoCzym == 'x':
                x = symbols('x')
                wynik = diff(Funkcja, x)
            if PoCzym == 'y':
                y = symbols('y')
                wynik = diff(Funkcja, y)
            if PoCzym == 'z':
                z = symbols('z')
                wynik = diff(Funkcja, z)
        except TypeError:
            return False
        else:
            string = str(wynik)
            print(string)
            if string.find('Derivative') > -1:
                return False
            return string

    def MiejsceZerowe(Funkcja):
        """
        Zero points of passed function.

        Parameters
        ----------
        Funkcja : string
            Function to be calculated.
        Returns
        -------
        bool -- "False" if 'diff' return error.
        string -- result of operation if there is not error.
        """
        try:
            x, y, z = symbols('x, y, z')
            wynik = solve(Funkcja)
        except TypeError:
            return False
        else:
            string = str(wynik)
            print(string)
            if string == "[]":
                string = "Brak miejsc zerowych"

            return string
