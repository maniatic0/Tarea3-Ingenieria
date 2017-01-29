# -*- coding: utf-8 -*-
'''
Created on Jan 28, 2017

@author: Christian Oliveros
@author: Daniel Varela
'''
from datetime import datetime
from builtins import str, int

class BilleteraElectronica(object):
    '''
    Clase que mantiene la Billetera Electronica de una Persona
    @ivar _identificador: Identificador de la persona
    @ivar _nombres: Nombres de la Persona
    @ivar _apellidos: Apellidos de la Persona
    @ivar _ci: Cedula de la Persona
    @ivar _pin: PIN secreto de la Persona
    @ivar _registroCreditos: Registro de Creditos de la Persona, contiene tripletas (monto, fecha, idLocal)
    @ivar _registoDebitos: Registro de Debitos de la Persona, contiene tripletas (monto, fecha, idLocal
    '''
    _identificador = None
    _nombres = ""
    _apellidos = ""
    _ci = -1
    _pin = None
    _registroCreditos = []
    _registoDebitos = []


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
        pass
    
    def recargar(self, monto, fecha, idLocal):
        pass
    
    def consumir(self, monto, fecha, idLocal, pin):
        pass
    
        