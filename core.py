# -*- coding: utf-8 -*-
"""
Created on Mon May 24 20:20:31 2021

@author: oxford
"""
from sympy import symbols, diff, integrate, solve, Function
f = Function('f')


class obliczenia():

    def calkowanie(Funkcja, PoCzym):
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

    def calkowanieOzn(Funkcja, PoCzym, od, do):
        if PoCzym == 'x':
            x = symbols('x')
            wynik = integrate(Funkcja, (x, od, do))
        if PoCzym == 'y':
            y = symbols('y')
            wynik = integrate(Funkcja, (y, od, do))
        if PoCzym == 'z':
            z = symbols('z')
            wynik = integrate(Funkcja, (z, od, do))

        print(wynik)
        string = str(wynik)
        print(string)
        return string

    def pochodna(Funkcja, PoCzym):
        if PoCzym == 'x':
            x = symbols('x')
            wynik = diff(Funkcja, x)
        if PoCzym == 'y':
            y = symbols('y')
            wynik = diff(Funkcja, y)
        if PoCzym == 'z':
            z = symbols('z')
            wynik = diff(Funkcja, z)

        string = str(wynik)
        print(string)
        return string

        string = str(wynik)
        print(string)
        return string

    def MiejsceZerowe(Funkcja):

        x, y, z = symbols('x, y, z')
        wynik = solve(Funkcja)

        string = str(wynik)
        print(string)
        return string
