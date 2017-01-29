# -*- coding: utf-8 -*-
'''
Created on Jan 28, 2017

@author: Christian Oliveros
@author: Daniel Varela
'''
from datetime import datetime

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


    def __init__(self, identificador, nombres, apellidos, ci, pin):
        '''
        Constructor
        '''
        pass
    
    def getIdentificador(self):
        pass
    
    def getNombres(self):
        pass
    
    def getApellidos(self):
        pass
    
    def getCI(self):
        pass
    
    def saldo(self):
        pass
    
    def recargar(self, monto, fecha, idLocal):
        pass
    
    def consumir(self, monto, fecha, idLocal, pin):
        pass
    
        