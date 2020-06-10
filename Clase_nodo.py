from Clase_vehiculo import Vehiculo
class Nodo():
    __vehiculo=None
    __siguiente=None
    def __init__(self,vehiculo):
        if isinstance(vehiculo,Vehiculo):
            self.__vehiculo=vehiculo
            self.__siguiente=None
        else:
            print("El objeto no era instancia de una clase valida")
            self.__vehiculo=-1
    def modificarSiguiente(self,siguiente):
        self.__siguiente=siguiente
    def getSiguiente(self):
        return self.__siguiente
    def getElemento(self):
        return self.__vehiculo
    def toJSON(self):
        return self.__vehiculo.toJSON()