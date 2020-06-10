from Clase_vehiculo import Vehiculo
class Usado(Vehiculo):
    __marca=""
    __patente=""
    __año=0
    __km=0
    def __init__(self,modelo,puertas,color,preciobase,marca,patente,año,km):
        super().__init__(modelo,puertas,color,preciobase)
        self.__marca=marca
        self.__patente=patente
        self.__año=año
        self.__km=km
    def calcularImporteVenta(self):
        antiguedad=2020-self.__año
        importe=super().getPrecio()-((antiguedad*super().getPrecio())/100)
        if(self.__km>100000):
            importe-=(2*super().getPrecio())/100
        return importe
    def getPatente(self):
        return self.__patente
    def modificarPrecioBase(self,precio):
        super().modificaPrecio(precio)
    def mostrarDatosUsado(self):
        cadena=self.__str__()+self.mostrarDatos()+" Marca:{} Patente:{} Año:{} KM:{}".format(self.__marca,self.__patente,self.__año,self.__km)
        return cadena
    def toJSON(self):
        d=dict(__class__=self.__class__.__name__,__atributos__=dict(modelo=super().getModelo(),puertas=super().getPuertas(),color=super().getColor(),preciobase=super().getPrecio(),marca=self.__marca,patente=self.__patente,año=self.__año,km=self.__km))
        return d             