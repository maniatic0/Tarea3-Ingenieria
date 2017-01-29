# -*- coding: utf-8 -*-
'''
Created on Jan 28, 2017

@author: Christian Oliveros
@author: Daniel Varela
'''
import unittest
from billeteraElectronica import BilleteraElectronica

class Test(unittest.TestCase):
    
    def helperConstructorTest(self, identificador, nombres, apellidos, ci, pin):
        '''
        Funcion de apoyo para probar construcion de clase correcta
        @param identificador: Identificador de la Persona
        @param nombres: Nombres de la Persona
        @param apellidos: Apellidos de la Persona
        @param ci: Cedula de la Persona
        @param pin: PIN de la Billetera de la Persona
        '''
        billetera = BilleteraElectronica(identificador, nombres, apellidos, ci, pin)
        self.assertEqual(billetera.getIdentificador(), identificador, "Identificador Distinto")
        self.assertEqual(billetera.getNombres(), nombres, "Nombres Distintos")
        self.assertEqual(billetera.getApellidos(), apellidos, "Apellidos Distintos")
        self.assertEqual(billetera.getCI(), ci, "CI Distintas")
        self.assertEqual(billetera._pin, pin, "PIN Distinto")
        
    def testConstruccion(self):
        '''Caso Interior'''
        self.helperConstructorTest(1, "Juan", "Gomez", 24666888, 1234)

    def testConstruccionConUnicode(self):
        '''Caso Interior'''
        self.helperConstructorTest(1, "Adèle", "Gómez", 300, 1324)
        
    def testConstruccionConVariosNombresYApellidos(self):
        '''Caso Interior'''
        self.helperConstructorTest(1, "Adèle Alexia", "Gómez Ñañe", 700000000, 3000)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()