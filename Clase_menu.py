from Clase_nuevo import Nuevo
from Clase_usado import Usado
class Menu:
    __switcher=None
    def __init__(self):
        self.__switcher = { 1:self.opcion1,
                            2:self.opcion2,
                            3:self.opcion3,
                            4:self.opcion4,
                            5:self.opcion5,
                            6:self.opcion6,
                            7:self.opcion7,
                            8:self.opcion8,
                            9:self.salir
                         }
    def opcion(self,op,manejador,jsonf):
        func=self.__switcher.get(op, lambda: print("Opción no válida"))
        if(op<1 or op>8):    
            func()
        else:
            if(op==7):
                func(manejador,jsonf)
            else:
                func(manejador)
    def salir(self):
        print('Usted salio del programa')
    def CargaDeDatos(self):
        modelo=input("Ingrese modelo:")  
        puertas=int(input("Ingrese cantidad de puertas:"))
        color=input("Ingrese color:")  
        preciobase=int(input("Ingrese precio base del vehiculo:"))
        opcion=int(input("Ingrese 1 si el vehículo es usado o 2 para nuevo:"))
        auto=None
        while(opcion!=1 and opcion !=2):
            print("Opción incorrecta")
            opcion=int(input("Ingrese 1 para usado o 2 para nuevo"))
        if opcion==1:
            marca=input("Ingrese marca:")
            patente=input("Ingrese patente:")
            año=int(input("Ingrese año:"))
            km=int(input("Ingrese km del vehiculo:"))
            auto=Usado(modelo,puertas,color,preciobase,marca,patente,año,km)
        else: 
            if(Nuevo.marca==""):
                print("Por ser el primer auto a registrar nuevo se debe indicar la marca de los mismos")
                Marca=input("Ingrese marca:")
                Nuevo.marca=Marca
            version=int(input("Ingrese 1 para versión base o 2 para full:"))
            while(version!=1 and version !=2):
                print("Opción incorrecta")
                version=int(input(("Ingrese 1 para versión base o 2 para full:")))
            if(version==1):
                version="base"
            else:
                version="full"
            auto=Nuevo(modelo, puertas, color, preciobase, version)
        return auto
    def opcion1(self,manejador):
        auto=self.CargaDeDatos()
        pos=int(input("Ingrese la posición a añadir en la lista:"))
        error=manejador.insertarEnLista(auto,pos)
        while(error==-1):
            pos=int(input("Ingrese posicion a añadir en la lista que resulte correcta:"))
            error=manejador.insertarEnLista(auto,pos)
    def opcion2(self,manejador):
        auto=self.CargaDeDatos()
        manejador.agregarEnLista(auto)
    def opcion3(self,manejador):
        pos=int(input("Ingrese la posición:"))
        manejador.mostrarElemento(pos)
    def opcion4(self,manejador):
        patente=input("Ingrese la patente:")
        precio=int(input("Ingrese el nuevo precio:"))
        manejador.modificarPrecioBase(patente,precio)
    def opcion5(self,manejador):
        manejador.mostrarVehiculoEconomico()
    def opcion6(self,manejador):
        manejador.mostrarVehiculos()
    def opcion7(self,manejador,jsonf):
        manejador.guardarenJson(jsonf,"vehiculos.json")
    def opcion8(self,manejador):
        manejador.test()