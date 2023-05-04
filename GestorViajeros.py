from Viajero import ViajeroFrecuente
import csv

class GestorViajeros:
    def __init__(self):
        self.__listaViajeros= []

    def agregarViajero(self,viajero):
        self.__listaViajeros.append(viajero)
    
    def leerArchivo(self): 
        File = open('archivo.csv')
        reader = csv.reader(File,delimiter=',')
        for row in reader:
            num_viajero= int(row[0])
            dni = row[1]
            nombre = row[2]
            apellido = row[3]
            millas_acum = int(row[4])
            UnViajero= ViajeroFrecuente(num_viajero,dni,nombre,apellido,millas_acum)
            self.agregarViajero(UnViajero)
        File.close()
    def buscarViajero(self,viajero):
        for v in self.__listaViajeros:
            if v.getNum()==viajero:
                return v
    def obtenerViajerosMayor(self):
        mayor=int(self.__listaViajeros[0].cantidadMillas())
        for i in range(len(self.__listaViajeros)-1):
            if self.__listaViajeros[i]>self.__listaViajeros[i+1]:
                m=self.__listaViajeros[i].cantidadMillas()
        for k in range(len(self.__listaViajeros)):
            if m==self.__listaViajeros[k].cantidadMillas():
                print(self.__listaViajeros[k])

    def acumularMillas(self,viajero,millas):
        viajero=viajero+millas
        print(viajero.cantidadMillas())
    def canjearMillas(self,viajero,millas):
        viajero=viajero-millas
        print(viajero.cantidadMillas())
    def __str__(self):
        v=''
        for viajero in self.__listaViajeros:
            v+= str(viajero) + '\n'
        return v
