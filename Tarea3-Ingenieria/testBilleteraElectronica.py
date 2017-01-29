# -*- coding: utf-8 -*-
'''
Created on Jan 28, 2017

@author: Christian Oliveros
@author: Daniel Varela
'''
import unittest
from datetime import datetime
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
        billetera.recargar(100,datetime.today(),909091)
        self.assertEqual(billetera.saldo(),100,"Recarga Saldo Distinto")
        
    def testConsumirSaldo(self):
        '''Caso Interior'''
        billetera = BilleteraElectronica(1,"Cesar","Jose",10231940,5901)
        billetera.consumir(-15,datetime.today(),843213,5901)
        self.assertEqual(billetera.saldo(),-15,"Consumo Saldo Distinto")
        
    def testRegistroCredito(self):
        '''Caso Interior'''
        billetera = BilleteraElectronica(1,"Ricardo","Gomez",26697166,6412)
        fecha = datetime.today()
        billetera.recargar(200,fecha,666999)
        tamano = len(billetera._registroCreditos)-1
        self.assertEqual(billetera._registroCreditos[tamano][0],200,"Registro Credito Saldo Distinto")
        self.assertEqual(billetera._registroCreditos[tamano][1],fecha,"Registro Credito Fecha Distinto")
        self.assertEqual(billetera._registroCreditos[tamano][2],666999,"Registro Credito idLocal Distinto")
        
    def testRegistroDebito(self):
        '''Caso Interior'''
        billetera = BilleteraElectronica(1,"Oscar","Silva",9039084,10120)
        fecha = datetime.today()
        billetera.consumir(-300,fecha,131141,10120)
        tamano = len(billetera._registroDebitos)-1
        self.assertEqual(billetera._registroDebitos[tamano][0],-300,"Registro Debito Saldo Distinto")
        self.assertEqual(billetera._registroDebitos[tamano][1],fecha,"Registro Debito Fecha Distinto")
        self.assertEqual(billetera._registroDebitos[tamano][2],131141,"Registro Debito idLocal Distinto")
        
    def testExcepcionRecargarSaldoNegativo(self):
        '''Caso Borde'''
        with self.assertRaises(Exception) as context:
            billetera = BilleteraElectronica(1,"Vicente","Neruda",342501,2346)
            fecha = datetime.today()
            billetera.recargar(-420,fecha,745)
            self.assertTrue("Monto tiene que ser un numero positivo" in str(context.exception))
            
    def testExceptionRecargarSaldoFechaFormatoIncorrecto(self):
        '''Caso Borde'''
        with self.assertRaises(Exception) as context:
            billetera = BilleteraElectronica(1,"Enrique","Guzman",77562,9000)
            fecha = '2017/01/25'
            billetera.recargar(777,fecha,0)
            self.assertTrue("Fecha tiene que ser un datetime " in str(context.exception)) 
            
    def testExceptionConsumirSaldoPositivo(self):
        '''Caso Borde'''
        with self.assertRaises(Exception) as context:
            billetera = BilleteraElectronica(1,"Pedro","Domingo",92031,834)
            fecha = datetime.today()
            billetera.consumir(10,fecha,666)
            self.assertTrue("Monto tiene que ser un numero negativo" in str(context.exception))
            
    def testExceptionConsumirSaldoFechaFormatoIncorrecto(self):
        '''Caso Borde'''
        with self.assertRaises(Exception) as context:
            billetera = BilleteraElectronica(1,"Jesus","Salom",145020,69)
            fecha = (2017,12,24)
            billetera.recargar(550,fecha,2670,69)
            billetera.consumir(-500,fecha,2670,69)
            self.assertTrue("Fecha tiene que ser un datetime " in str(context.exception))
            
    def testExceptionConsumirSaldoPinDistinto(self):
        '''Caso Borde'''
        with self.assertRaises(Exception) as context:
            billetera = BilleteraElectronica(1,"Gustavo","Blanco",64212,35967)
            fecha = datetime.today()
            billetera.consumir(250,fecha,23012)
            billetera.consumir(-202,fecha,23012,7)
            self.assertTrue("Error, el pin introducido no corresponde con la billetera del usuario registrado" in str(context.exception))
     
    def testExceptionConsumirSaldoInsuficiente(self):
        '''Caso Borde'''
        with self.assertRaises(Exception) as context:
            billetera = BilleteraElectronica(1,"Juan","Betancourt",293012,394)
            fecha = datetime.today()
            billetera.recargar(200,fecha,49292)
            billetera.consumir(-999,fecha,49202,394)
            self.assertTrue("Error, no se cuenta con balance suficiente para cubrir el coste de la operacion" in str(context.exception))
        
    def testExceptionConsumirSaldoPinNulo(self):
        '''Caso Borde'''
        with self.assertRaises(Exception) as context:
            billetera = BilleteraElectronica(1,"Noel","Rodriguez",56347,12122)
            fecha = datetime.today()
            billetera.recargar(20,fecha,15010)
            billetera.consumir(-19,fecha,20100)
            self.assertTrue("Debe introducir un pin de usuario" in str(context.exception))
    
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
    
    