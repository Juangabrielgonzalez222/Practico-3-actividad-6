from Clase_vehiculo import Vehiculo
class Nuevo(Vehiculo):
    marca=""
    __version=""
    def __init__(self,modelo,puertas,color,preciobase,version):
        super().__init__(modelo,puertas,color,preciobase)
        self.__version=version
    def calcularImporteVenta(self):
        importe=super().getPrecio() + ((10*super().getPrecio())/100)
        if(self.__version=="full"):
            importe+=(2*super().getPrecio())/100
        return importe
    def getMarca(cls):
        return cls.marca
    def mostrarDatosNuevo(self):
        cadena=self.__str__()+self.mostrarDatos()+"Marca:{} Version:{}".format(self.getMarca(),self.__version)
        return cadena
    def toJSON(self):
        d=dict(__class__=self.__class__.__name__,__atributos__=dict(modelo=super().getModelo(),puertas=super().getPuertas(),color=super().getColor(),preciobase=super().getPrecio(),marca=self.getMarca(),version=self.__version))
        return d