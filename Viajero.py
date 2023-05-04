import csv
class ViajeroFrecuente:
    __num_viajero= int
    __dni = str
    __nombre = str
    __apellido = str
    __millas_acum = int
    def __init__(self, num_viajero=0,dni='',nombre='',apellido='', millas_acum=0):
        self.__num_viajero= num_viajero
        self.__dni = dni
        self.__nombre = nombre
        self.__apellido = apellido
        self.__millas_acum = millas_acum
    def getNum(self):
        return self.__num_viajero
    def cantidadMillas(self):
        return self.__millas_acum
    def __gt__(self,otroViajero):
        return self.__millas_acum>otroViajero.__millas_acum
    def __add__(self,otro):
        return ViajeroFrecuente(self.__num_viajero,self.__dni,self.__nombre,self.__apellido,self.__millas_acum+otro)
    def __sub__(self,otro):
        return ViajeroFrecuente(self.__num_viajero,self.__dni,self.__nombre,self.__apellido,self.__millas_acum-otro)
    def __str__(self):
        return '%s %s %s %s %s'%(self.__num_viajero,self.__dni,self.__nombre,self.__apellido,self.__millas_acum)