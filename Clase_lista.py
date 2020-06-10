from zope.interface import implementer
from interface import Interface1
from Clase_nodo import Nodo
@implementer(Interface1)
class Lista():
    __comienzo=None
    __actual=None
    __indice=0
    __tope=0
    def __init__(self):
        self.__comienzo=None
        self.__actual=None
        self.__indice=0
        self.__tope=0
    def __iter__(self):
        return self
    def __next__(self):
        if self.__indice==self.__tope:
            self.__actual=self.__comienzo
            self.__indice=0
            raise StopIteration
        else:
            self.__indice+=1
            dato=self.__actual.getElemento()
            self.__actual=self.__actual.getSiguiente()
            return dato
    def insertarElemento(self,elemento,pos):
        error=None
        try:
            if(pos>self.__tope+1 or pos<1):
                raise IndexError
        except IndexError:
            print("La posición indicada no es correcta,ingrese posición del 1-{}".format(self.__tope+1))
            error=-1
        else:
            nodo=Nodo(elemento)
            verificar=nodo.getElemento()
            if(verificar!=-1):
                if(pos==1):
                    nodo.modificarSiguiente(self.__comienzo)
                    self.__comienzo=nodo
                    self.__tope+=1
                    self.__actual=self.__comienzo
                elif(pos==self.__tope+1):
                    self.agregarElemento(elemento)
                else:               
                    i=0              
                    siguiente=self.__comienzo
                    anterior=self.__comienzo
                    while(i<pos-1):
                        anterior=siguiente            
                        siguiente=siguiente.getSiguiente()
                        i+=1
                    anterior.modificarSiguiente(nodo)
                    nodo.modificarSiguiente(siguiente)
                    self.__tope+=1
        return error
    def agregarElemento(self,elemento):
        nodo=Nodo(elemento)
        verificar=nodo.getElemento()
        if(verificar!=-1):
            if(self.__comienzo==None):
                self.__comienzo=nodo
                self.__actual=self.__comienzo
            else:
                aux=self.__comienzo
                while(aux.getSiguiente()!=None):
                    aux=aux.getSiguiente()
                aux.modificarSiguiente(nodo)
            self.__tope+=1
    def mostrarElemento(self,pos):
        from Clase_nuevo import Nuevo
        try:
            if(pos>self.__tope or pos<1):
                raise IndexError
        except IndexError:
            print("La posición indicada no es correcta,ingrese posición del 1-{}".format(self.__tope))
        else:
            tipo=None
            if(pos==1):
                nodo=self.__comienzo.getElemento()
                tipo=type(nodo)
            else:
                aux=self.__comienzo
                for i in range(0,pos-1): 
                    aux=aux.getSiguiente() 
                aux=aux.getElemento()
                tipo=type(aux)
            if(tipo==Nuevo):
                print("En la posición ",pos," el tipo de vehiculo es nuevo")
            else:
                print("En la posición ",pos," el tipo de vehiculo es usado")
    def getComienzo(self):
        return self.__comienzo