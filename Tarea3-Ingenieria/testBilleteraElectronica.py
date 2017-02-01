# -*- coding: utf-8 -*-
'''
Created on Jan 28, 2017

@author: Christian Oliveros
@author: Daniel Varela
'''
import unittest
from datetime import datetime
from billeteraElectronica import BilleteraElectronica
import sys

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
     
    def testConstruccionNombreBorde(self):
        '''Caso Borde'''
        self.helperConstructorTest(1, "Á", "Borges", 50, 3000)
    
    def testConstruccionApellidoBorde(self):
        '''Caso Borde'''
        self.helperConstructorTest(1, "Alonzo", "B", 5, 6552)
        
    def testConstruccionCIBorde(self):
        '''Caso Borde'''
        self.helperConstructorTest(1, "Marcus", "Persson", 1, 74555)
        
    def testConstruccionPINBorde(self):
        '''Caso Borde'''
        self.helperConstructorTest(1, "Franz", "Kafka", 455, 0)
     
    def testConstruccionNombreApellidoEsquina(self):
        '''Caso Esquina'''
        self.helperConstructorTest(1, "Á", "Ü", 666, 9999)
        
    def testConstruccionNombreApellidoUnicodeEsquina(self):
        '''Caso Esquina'''
        self.helperConstructorTest(1, "宮本 茂", "Лев Никола́евич Толсто́й", 24601, 0000)
    
    def testConstruccionTotalEsquina(self):
        '''Caso Esquina'''
        self.helperConstructorTest(1, "宮", "Л", 1, 0)
     
    def testConstruccionSinNombre(self):
        '''Caso Invalido'''
        with self.assertRaises(Exception) as context:
            BilleteraElectronica(1,"","Neruda",342501,2346)
            self.assertTrue("Nombres tiene que ser un String no Vacio" in str(context.exception))
    
    def testConstruccionSinApellidos(self):
        '''Caso Invalido'''
        with self.assertRaises(Exception) as context:
            BilleteraElectronica(1,"Pablo","",34251,246)
            self.assertTrue("Apellidos tiene que ser un String no Vacio" in str(context.exception))
    
    def testConstruccionCedulaInvalida(self):
        '''Caso Invalido'''
        with self.assertRaises(Exception) as context:
            BilleteraElectronica(1,"Perejil","Mene",0,26)
            self.assertTrue("Cedula tiene que ser un Entero mayor que Cero" in str(context.exception))
      
    def testConstruccionPINInvalido(self):
        '''Caso Invalido'''
        with self.assertRaises(Exception) as context:
            BilleteraElectronica(1,"Franco","De Vita",122,-1)
            self.assertTrue("PIN tiene que ser un Entero mayor o igual que Cero" in str(context.exception))  
      
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
        billetera.recargar(16,datetime.today(),19203)
        billetera.consumir(-15,datetime.today(),843213,5901)
        self.assertEqual(billetera.saldo(),1,"Consumo Saldo Distinto")
        
    def testRegistroCredito(self):
        '''Caso Interior'''
        billetera = BilleteraElectronica(1,"Ricardo","Gomez",26697166,6412)
        fecha = datetime.today()
        billetera.recargar(200,fecha,666999)
        tamano = len(billetera._registroCreditos)-1
        self.assertEqual(billetera._registroCreditos[tamano][0],200,"Registro Credito Saldo Distinto")
        self.assertEqual(billetera._registroCreditos[tamano][1],fecha,"Registro Credito Fecha Distinto")
        self.assertEqual(billetera._registroCreditos[tamano][2],666999,"Registro Credito idLocal Distinto")
        
    def testRegistroCreditoBorde(self):
        '''Caso Borde'''
        billetera = BilleteraElectronica(1,"Ricardo","Gomez",26697166,6412)
        fecha = datetime.today()
        billetera.recargar(sys.float_info.epsilon,fecha,666999)
        tamano = len(billetera._registroCreditos)-1
        self.assertEqual(billetera._registroCreditos[tamano][0],sys.float_info.epsilon,"Registro Credito Saldo Distinto")
        self.assertEqual(billetera._registroCreditos[tamano][1],fecha,"Registro Credito Fecha Distinto")
        self.assertEqual(billetera._registroCreditos[tamano][2],666999,"Registro Credito idLocal Distinto")
      
    def testRegistroDebito(self):
        '''Caso Interior'''
        billetera = BilleteraElectronica(1,"Oscar","Silva",9039084,10120)
        fecha = datetime.today()
        billetera.recargar(350,fecha,131141)
        billetera.consumir(-300,fecha,131141,10120)
        tamano = len(billetera._registroDebitos)-1
        self.assertEqual(billetera._registroDebitos[tamano][0],-300,"Registro Debito Saldo Distinto")
        self.assertEqual(billetera._registroDebitos[tamano][1],fecha,"Registro Debito Fecha Distinto")
        self.assertEqual(billetera._registroDebitos[tamano][2],131141,"Registro Debito idLocal Distinto")
        
    def testRegistroDebitoBorde(self):
        '''Caso Borde'''
        billetera = BilleteraElectronica(1,"Asdrubal","Oliveros",9039084,10120)
        fecha = datetime.today()
        billetera.recargar(sys.float_info.epsilon,fecha,131141)
        billetera.consumir(-sys.float_info.epsilon,fecha,131141,10120)
        tamano = len(billetera._registroDebitos)-1
        self.assertEqual(billetera._registroDebitos[tamano][0],-sys.float_info.epsilon,"Registro Debito Saldo Distinto")
        self.assertEqual(billetera._registroDebitos[tamano][1],fecha,"Registro Debito Fecha Distinto")
        self.assertEqual(billetera._registroDebitos[tamano][2],131141,"Registro Debito idLocal Distinto")
        
    def testSaldoFuncional(self):
        '''Caso Interior'''
        billetera = BilleteraElectronica(1,"Oscaruja","Mezartega",666,999)
        fecha = datetime.today()
        billetera.recargar(15,fecha,999)
        billetera.consumir(-12,fecha,131141,999)
        self.assertEqual(billetera.saldo(), 3, "Saldo Distinto")
        
    def testSaldoFuncionalBorde(self):
        '''Caso Borde'''
        billetera = BilleteraElectronica(1,"Oscaruja","Mezartega",666,999)
        fecha = datetime.today()
        billetera.recargar(sys.float_info.epsilon,fecha,999)
        billetera.consumir(-sys.float_info.epsilon,fecha,131141,999)
        self.assertEqual(billetera.saldo(), 0, "Saldo Distinto")
    
    def testExcepcionRecargarSaldoNegativo(self):
        '''Caso Invalido'''
        with self.assertRaises(Exception) as context:
            billetera = BilleteraElectronica(1,"Vicente","Neruda",342501,2346)
            fecha = datetime.today()
            billetera.recargar(-420,fecha,745)
            self.assertTrue("Monto tiene que ser un numero positivo" in str(context.exception))
            
    def testExceptionRecargarSaldoFechaFormatoIncorrecto(self):
        '''Caso Invalido'''
        with self.assertRaises(Exception) as context:
            billetera = BilleteraElectronica(1,"Enrique","Guzman",77562,9000)
            fecha = '2017/01/25'
            billetera.recargar(777,fecha,0)
            self.assertTrue("Fecha tiene que ser un datetime " in str(context.exception)) 
            
    def testExceptionConsumirSaldoPositivo(self):
        '''Caso Invalido'''
        with self.assertRaises(Exception) as context:
            billetera = BilleteraElectronica(1,"Pedro","Domingo",92031,834)
            fecha = datetime.today()
            billetera.consumir(10,fecha,666)
            self.assertTrue("Monto tiene que ser un numero negativo" in str(context.exception))
            
    def testExceptionConsumirSaldoFechaFormatoIncorrecto(self):
        '''Caso Invalido'''
        with self.assertRaises(Exception) as context:
            billetera = BilleteraElectronica(1,"Jesus","Salom",145020,69)
            fecha = (2017,12,24)
            billetera.recargar(550,fecha,2670,69)
            billetera.consumir(-500,fecha,2670,69)
            self.assertTrue("Fecha tiene que ser un datetime " in str(context.exception))
            
    def testExceptionConsumirSaldoPinDistinto(self):
        '''Caso Invalido'''
        with self.assertRaises(Exception) as context:
            billetera = BilleteraElectronica(1,"Gustavo","Blanco",64212,35967)
            fecha = datetime.today()
            billetera.consumir(250,fecha,23012)
            billetera.consumir(-202,fecha,23012,7)
            self.assertTrue("Error, el pin introducido no corresponde con la billetera del usuario registrado" in str(context.exception))
     
    def testExceptionConsumirSaldoInsuficiente(self):
        '''Caso Invalido'''
        with self.assertRaises(Exception) as context:
            billetera = BilleteraElectronica(1,"Juan","Betancourt",293012,394)
            fecha = datetime.today()
            billetera.recargar(200,fecha,49292)
            billetera.consumir(-999,fecha,49202,394)
            self.assertTrue("Error, no se cuenta con balance suficiente para cubrir el coste de la operacion" in str(context.exception))
        
    def testExceptionConsumirSaldoPinNulo(self):
        '''Caso Invalido'''
        with self.assertRaises(Exception) as context:
            billetera = BilleteraElectronica(1,"Noel","Rodriguez",56347,12122)
            fecha = datetime.today()
            billetera.recargar(20,fecha,15010)
            billetera.consumir(-19,fecha,20100)
            self.assertTrue("Debe introducir un pin de usuario" in str(context.exception))
            
    def testExceptionRecargaridLocalNulo(self):
        '''Caso Borde'''
        with self.assertRaises(Exception) as context:
            billetera = BilleteraElectronica(1,"Alfonso","Ramon",10293,39491)
            fecha = datetime.today()
            billetera.recargar(10,fecha)
            self.assertTrue("Debe introducir un idLocal" in str(context.exception))
            
    def testExceptionConsumiridLocalNulo(self):
        '''Caso Borde'''
        with self.assertRaises(Exception) as context:
            billetera = BilleteraElectronica(1,"Sartenejas","Simon",34,1023)
            fecha = datetime.today()
            billetera.recargar(21,fecha,101)
            billetera.consumir(-17,fecha,None,9002)
            self.assertTrue("Debe introducir in idLocal" in str(context.exception))
    
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
    
    