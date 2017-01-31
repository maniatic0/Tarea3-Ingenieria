# -*- coding: utf-8 -*-
'''
Created on Jan 28, 2017

@author: Christian Oliveros
@author: Daniel Varela
'''
from datetime import datetime
from builtins import str, int, float

class BilleteraElectronica(object):
    '''
    Clase que mantiene la Billetera Electronica de una Persona
    @ivar _identificador: Identificador de la persona
    @ivar _nombres: Nombres de la Persona
    @ivar _apellidos: Apellidos de la Persona
    @ivar _ci: Cedula de la Persona
    @ivar _pin: PIN secreto de la Persona
    @ivar _registroCreditos: Registro de Creditos de la Persona, contiene tripletas (monto, fecha, idLocal)
    @ivar _registroDebitos: Registro de Debitos de la Persona, contiene tripletas (monto, fecha, idLocal)
    '''
    _identificador = None
    _nombres = ""
    _apellidos = ""
    _ci = -1
    _pin = None
    _registroCreditos = []
    _registroDebitos = []


    def __init__(self, identificador, nombres: str, apellidos: str, ci: int, pin: int):
        '''
        Constructor de la Clase BilleteraElectronica
        @param identificador: Identificador de la Persona
        @param nombres: Nombres de la Persona
        @param apellidos: Apellidos de la Persona
        @param ci: Cedula de la Persona
        @param pin: PIN de la Billetera de la Persona
        '''
        if not isinstance(nombres, str) or nombres == "":
            raise Exception("Nombres tiene que ser un String no Vacio")
        
        if not isinstance(apellidos, str) or apellidos == "":
            raise Exception("Apellidos tiene que ser un String no Vacio")
        
        if not isinstance(ci, int) or ci <= 0:
            raise Exception("Cedula tiene que ser un Entero mayor que Cero")
        
        if not isinstance(pin, int) or pin < 0:
            raise Exception("PIN tiene que ser un Entero mayor o igual que Cero")
        
        self._identificador = identificador
        self._nombres = nombres
        self._apellidos = apellidos
        self._ci = ci
        self._pin = pin
        self._registroCreditos = []
        self._registroDebitos = []
    
    def getIdentificador(self):
        '''@return: Identificador de la Persona'''
        return self._identificador
    
    def getNombres(self):
        '''@return: Nombres de la Persona'''
        return self._nombres
    
    def getApellidos(self):
        '''@return: Apellidos de la Persona'''
        return self._apellidos
    
    def getCI(self):
        '''@return: CI de la Persona'''
        return self._ci
    
    def saldo(self):
        '''@return: Balance de saldo actual en la cuenta'''
        if (len(self._registroCreditos) == 0) and (len(self._registroDebitos) == 0):
            saldo_actual = 0
            return saldo_actual
        else:
            recarga_total = 0
            consumo_total = 0
            for i in range(len(self._registroCreditos)):
                recarga_total = recarga_total + self._registroCreditos[i][0]
            for i in range(len(self._registroDebitos)):
                consumo_total = consumo_total + self._registroDebitos[i][0]
        saldo_actual = recarga_total + consumo_total
        return saldo_actual
    
    def recargar(self, monto, fecha, idLocal):
        '''
        Realiza el registro del monto recargado
        @param monto: Monto a recargar, tiene que ser positivo
        @param fecha: Tiempo en el cual ocurrio la recarga
        @param idLocal: ID de lugar donde ocurrio la recarga
        '''
        if not isinstance(monto, (int, float)) or monto <= 0:
            raise Exception("Monto tiene que ser un numero positivo")
        
        if not isinstance(fecha, datetime):
            raise Exception("Fecha tiene que ser un datetime ")
        
        recarga = (monto,fecha,idLocal)
        self._registroCreditos.append(recarga)
    
    def consumir(self, monto, fecha, idLocal, pin):
        '''
        Realiza el registro del monto consumido
        @param monto: Monto a consumir, tiene que ser negativo
        @param fecha: Tiempo en el cual ocurrio el consumo
        @param idLocal: ID de lugar donde ocurrio el consumo
        @param pin: PIN de la persona
        '''
        if not isinstance(monto, (int, float)) or monto > 0:
            raise Exception("Monto tiene que ser un numero negativo")
        
        if not isinstance(fecha, datetime):
            raise Exception("Fecha tiene que ser un datetime ")
        
        if idLocal == None:
            raise Exception("Debe introducir un idLocal")
        
        if pin == None:
            raise Exception("Debe introducir un pin de usuario")
        
        if self._pin != pin:
            raise Exception("Error, el pin introducido no corresponde con la billetera del usuario registrado") 
        
        if self.saldo() < abs(monto):
            raise Exception("Error, no se cuenta con balance suficiente para cubrir el coste de la operacion")
        
        consumo = (monto,fecha,idLocal)
        self._registroDebitos.append(consumo)
    
        