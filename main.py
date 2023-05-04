from Viajero import ViajeroFrecuente 
from GestorViajeros import GestorViajeros as GV
from menu import MenuOpciones as Menu
def test():
    gestor = GV()
    gestor.leerArchivo()
    print(gestor)
    menu= Menu()
    menu.opciones(gestor)

if __name__ == '__main__':
    test()