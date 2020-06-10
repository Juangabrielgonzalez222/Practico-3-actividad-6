import abc
class Vehiculo():
    __modelo=""
    __puertas=0
    __color=""
    __preciobase=0
    def __init__(self,modelo,puertas,color,preciobase):
        self.__modelo=modelo
        self.__puertas=puertas
        self.__color=color
        self.__preciobase=preciobase
    def getModelo(self):
        return self.__modelo
    def getPuertas(self):
        return self.__puertas
    def getColor(self):
        return self.__color
    def getPrecio(self):
        return self.__preciobase
    def modificaPrecio(self,precio):
        self.__preciobase=precio
    @abc.abstractmethod
    def calcularImporteVenta():
        pass
    @abc.abstractmethod
    def toJSON():
        pass
    def __str__(self):
        cadena=" Modelo:{} Cant.puertas:{} Importe de venta:{:.2f} ".format(self.__modelo,self.__puertas,self.calcularImporteVenta())
        return cadena
    def mostrarDatos(self):
        return " Color:{} Precio base: {} ".format(self.__color,self.__preciobase)
    