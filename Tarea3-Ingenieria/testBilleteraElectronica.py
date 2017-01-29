# -*- coding: utf-8 -*-
'''
Created on Jan 28, 2017

@author: Christian Oliveros
@author: Daniel Varela
'''
import unittest
from datetime import date
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
        
    def testBalanceSaldo(self):
        billetera = BilleteraElectronica(1,"Alexander","Infante",13102741,4200)
        self.assertEqual(billetera.saldo(),0,"Balance Saldo Distinto")
        
    def testRecargaSaldo(self):
        '''Caso Interior'''
        billetera = BilleteraElectronica(1,"John","Palma",26007718,1337)
        billetera.recargar(100,date.today(),909091)
        self.assertEqual(billetera.saldo(),100,"Recarga Saldo Distinto")
        
    def testConsumirSaldo(self):
        '''Caso Interior'''
        billetera = BilleteraElectronica(1,"Cesar","Jose",10231940,5901)
        billetera.consumir(-15,date.today(),843213,5901)
        self.assertEqual(billetera.saldo(),-15,"Consumo Saldo Distinto")
        
    def testRegistroCredito(self):
        '''Caso Interior'''
        billetera = BilleteraElectronica(1,"Ricardo","Gomez",26697166,6412)
        billetera.recargar(200,date.today(),666999)
        tamano = len(billetera._registroCreditos)-1
        self.assertEqual(billetera._registroCreditos[tamano][0],200,"Registro Saldo Distinto")
        self.assertEqual(billetera._registroCreditos[tamano][1],date.today(),"Registro Fecha Distinto")
        self.assertEqual(billetera._registroCreditos[tamano][2],666999,"Registro IDlocal Distinto")
        
    def testRegistroDebito(self):
        '''Caso Interior'''
        billetera = BilleteraElectronica(1,"Oscar","Silva",9039084,10120)
        billetera.consumir(-300,date.today(),131141,10120)
        tamano = len(billetera._registroCreditos)-1
        self.assertEqual(billetera._registroCreditos[tamano][0],-300,"Registro Saldo Distinto")
        self.assertEqual(billetera._registroCreditos[tamano][1],date.today(),"Registro Fecha Distinto")
        self.assertEqual(billetera._registroCreditos[tamano][2],date.today(),"Registro IDlocal Distinto")
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
    
    