from Clase_lista import Lista
from Clase_usado import Usado
from Clase_nuevo import Nuevo
from Clase_ObjectEncoder import ObjectEncoder
class Manejador():
    __lista=None   
    __jsonf=None
    __archivo=""
    def __init__(self):
            self.__lista=Lista()
            self.__jsonf=ObjectEncoder()
            self.__archivo="vehiculos.json"
    def insertarEnLista(self,elemento,pos):
        error=self.__lista.insertarElemento(elemento,pos)
        return error
    def agregarEnLista(self,elemento):
        self.__lista.agregarElemento(elemento)
    def mostrarElemento(self,pos):
        self.__lista.mostrarElemento(pos)
    def modificarPrecioBase(self,patente,preciobase):
        aux=self.__lista.getComienzo()
        bandera=True
        while(aux!=None and bandera):
            auto=aux.getElemento()
            if(type(auto)==Usado):
                if(auto.getPatente()==patente):
                    auto.modificarPrecioBase(preciobase)
                    print("Nuevo precio de venta:",auto.calcularImporteVenta())
                    bandera=False 
            aux=aux.getSiguiente()
        if bandera:
            print("No se encontro la patente")
    def mostrarVehiculoEconomico(self):
        comienzo=self.__lista.getComienzo()
        if(comienzo!=None):
            aux=comienzo.getSiguiente()
            barato=comienzo.getElemento()
            while(aux!=None):
                auto=aux.getElemento()
                if(auto.calcularImporteVenta()<barato.calcularImporteVenta()):
                    barato=auto
                aux=aux.getSiguiente()
            if(type(barato)==Nuevo):
                print(barato.mostrarDatosNuevo())
            else:
                print(barato.mostrarDatosUsado())
        else:
            print("No hay ningún vehículo en la lista")
    def toJson(self):
        d=dict(__class__=self.__class__.__name__,vehiculos=[auto.toJSON() for auto in self.__lista])
        return d
    def mostrarVehiculos(self):
        print("Vehículos:")
        for elemento in self.__lista:
            print(elemento)
    def guardarenJson(self,jsonf,archivo):
        if type(jsonf)==ObjectEncoder:
            dic=self.toJson()
            jsonf.guardarEnArchivo(dic,archivo)
            print("Se guardo con exito en el archivo")
        else:
            print("El parámetro recibido no es valido. ")
    def test(self):
        manejador2=Manejador()
        marca=Nuevo.marca
        jsonf=ObjectEncoder()
        Nuevo.marca=="Fiat"
        nuevo=Nuevo("Fiat-134", 4,"Rojo",500000,"full")
        usado=Usado("Ford 304",2,"Azul",400500,"Ford","ABC123",2000,200000)
        manejador2.insertarEnLista(nuevo,1)
        manejador2.agregarEnLista(usado)
        print("Vehículos en lista:")
        manejador2.mostrarVehiculos()
        print("Tipo de último auto:")
        manejador2.mostrarElemento(2)
        print("Cambio de precio base a vehículo usado, con 300000 ")
        manejador2.modificarPrecioBase("ABC123",300000)
        print("Vehículo mas económico: ")
        manejador2.mostrarVehiculoEconomico()
        print("Guardado de vehículos en prueba.json")
        manejador2.guardarenJson(jsonf,"prueba.json")
        Nuevo.marca=marca
        