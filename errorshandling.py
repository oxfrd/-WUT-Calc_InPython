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
    """
    Class of holding errors .

    This class is handling error events and incorrect data.
    """

    def __init__(self):
        """Constructo of class MainWin."""
        super(bledy, self).__init__()

    def PoprawneDaneIntDif(self, fun, poCzym):
        """
        Validate input data of integrating and derivative.

        Parameters
        ----------
        fun : string
            Function to check.
        poCzym : string
            Variable to check.

        Returns
        -------
        bool
            'True' -- data is valid.
            'False' -- data not valid
        """
        if bledy.brakFunkcji(self, fun) is False:
            return False

        if bledy.brakWarunku(self, poCzym) is False:
            return False

        if bledy.zlyWarunek(self, poCzym) is False:
            return False

        return True

    def bladWykresu(self):
        """
        Show popup when there is plot function error.

        Returns
        -------
        bool
            'False' and pop-up.

        """
        QMessageBox.critical(self, 'Błąd!',
                             "Wprowadź poprawną funkcję!")
        return False

    def PoprawneDaneRow(self, fun):
        """
        Validate data of zero points.

        Parameters
        ----------
        fun : string
            Function to check.

        Returns
        -------
        bool
            'True' -- data is valid
            'False' -- data not valid
        """
        if bledy.brakFunkcji(self, fun) is False:
            return False
        return True

    def zlaFunkcja(self):
        """
        Generate pop-up when fun is used.

        Returns
        -------
        Pop-up

        """
        QMessageBox.critical(self, 'Błąd',
                             "Wprowadź poprawną funkcję!")
        return

    def brakFunkcji(self, tekst):
        """
        Check if there is function passed.

        Parameters
        ----------
        tekst : string
            Function to check.

        Returns
        -------
        bool
            'True' -- there is data.
            'False' and pop-up -- there is not any data

        """
        if len(tekst) == 0:
            QMessageBox.critical(self, 'Błąd',
                                 "Wprowadź poprawną funkcję!")
            return False
        return True

    def brakWarunku(self, tekst):
        """
        Check if there is variable passed.

        Parameters
        ----------
        tekst : string
            Variable to check.
        Returns
        -------
        bool
            'True' -- there is data.
            'False' and pop-up -- there is not any data

        """
        if len(tekst) == 0:
            QMessageBox.critical(self, 'Błąd',
                                 "Wprowadź zmienną!")
            return False
        return True

    def zlyWarunek(self, tekst):
        """
        Check if variable is valid.

        Parameters
        ----------
        tekst : string
            Variable to check.
        Returns
        -------
        bool
            'True' -- there is valid data.
            'False' and pop-up -- there is not valid data
        """
        if tekst != 'x' and tekst != 'y' and tekst != 'z':
            QMessageBox.critical(self, 'Błąd',
                                 "Wprowadź poprawną zmienną (x, y lub z)!")

            return False
        return True

    def zlaCalkaOzn(self):
        """
        Check if function is valid.

        Parameters
        ----------
        tekst : string
            Function to check.
        Returns
        -------
        bool
            'True' -- there is valid data.
            'False' and pop-up -- there is not valid data
        """
        QMessageBox.critical(self, 'Błąd!',
                             "Wprowadź poprawną funkcję!")
        return False

    def sprawdzOdDO(self, tekst, tekst2):
        """
        Check if conditions of definite integral are valid.

        'From' is smaller than 'to', both of them are passed,
        there is possible to transform them to 'int' or 'float',
        or they are 'pi', logaritms or trigonometric fun.

        Parameters
        ----------
        tekst : string
            Integrate 'from' to check.
        tekst2 : string
            Integrate 'to' to check.

        Returns
        -------
        bool
            'True' -- there is valid data.
            'False' and pop-up -- there is not valid data
        """
        exception = False
        try:
            od = int(tekst)
        except ValueError:
            try:
                od = float(tekst)
            except ValueError:
                if tekst.find('pi') > -1 or tekst.find('sqrt') > -1                                 or tekst.find('log') > -1 or tekst.find('ln') > -1                                                  or tekst.find('sin') > -1 or tekst.find("cos") > -1                                             or tekst.find('tan') > -1 or tekst.find('ctan') > -1:
                    exception = True
                else:
                    QMessageBox.critical(self, 'Błąd! [1]',
                                         "Wprowadź poprawne warunki brzegowe!")
                    return False
            else:
                pass
        else:
            pass

        try:
            do = int(tekst2)
        except ValueError:
            try:
                do = float(tekst2)
            except ValueError:
                if tekst.find('pi') > -1 or tekst.find('sqrt') > -1                                     or tekst.find('log') > -1 or tekst.find('ln') > -1                                                      or tekst.find('sin') > -1 or tekst.find("cos") > -1                                                                     or tekst.find('tan') > -1 or tekst.find('ctan') > -1:
                    exception = True
                else:
                    QMessageBox.critical(self, 'Błąd! [1]',
                                         "Wprowadź poprawne warunki brzegowe!")
                    return False
            else:
                pass
        else:
            pass

        if len(tekst) == 0 or len(tekst2) == 0:

            QMessageBox.critical(self, 'Błąd! [3]',
                                 "Wprowadź poprawne warunki brzegowe!")
            return False

        if (exception is False) and (od > do):

            QMessageBox.critical(self, 'Błąd! [4]',
                                 "Wartosć 'od' jest większa niż 'do'. Zweryfikuj dane warunki brzegowe")
            return False
        else:
            return
