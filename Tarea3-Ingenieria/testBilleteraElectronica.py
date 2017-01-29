# -*- coding: utf-8 -*-
'''
Created on Jan 28, 2017

@author: Christian Oliveros
@author: Daniel Varela
'''
import unittest
from billeteraElectronica import BilleteraElectronica

class Test(unittest.TestCase):


    def testConstruccion(self):
        billetera = BilleteraElectronica(1, "Juan", "Gomez", 24666888, 1234)
        self.assertEqual(billetera.getIdentificador(), 1, "Identificador Distinto")
        self.assertEqual(billetera.getNombres(), "Juan", "Nombres Distintos")
        self.assertEqual(billetera.getApellidos(), "Gomez", "Apellidos Distintos")
        self.assertEqual(billetera.getCI()(), 24666888, "CI Distintas")
        self.assertEqual(billetera._pin, 1234, "PIN Distinto")


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()