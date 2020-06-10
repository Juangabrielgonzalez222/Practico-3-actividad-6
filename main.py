from Clase_menu import Menu
from Clase_manejador import Manejador
from Clase_ObjectEncoder import ObjectEncoder
if __name__=='__main__':
    jsonf=ObjectEncoder()
    diccionario=jsonf.leerArchivo("vehiculos.json")
    if diccionario!=-1:
        manejador=jsonf.DecodificarDiccionario(diccionario)
        print("Se cargaron vehículos de archivo")
    else:    
        manejador=Manejador()
    menu=Menu()
    op=None
    print("Bienvenido al programa:")
    while(op!=9):
        print("Ingrese 1 para insertar un vehículo en la colección en una posición determinada.")
        print("Ingrese 2 para agregar un vehículo al final de la colección.")
        print("Ingrese 3 para mostrar por pantalla qué tipo de objeto se encuentra almacenado en una posición.")
        print("Ingrese 4 para dada la patente de un vehículo usado, modificar su precio base.")
        print("Ingrese 5 para mostrar todos los datos del vehiculo mas económico.")
        print("Ingrese 6 para mostrar datos para todos los vehículos.")
        print("Ingrese 7 para almacenar los objetos de la colección en el archivo.")
        print("Ingrese 8 para realizar test.")
        print("Ingrese 9 para salir.")
        op=int(input("Ingrese opcion:"))
        menu.opcion(op,manejador,jsonf)