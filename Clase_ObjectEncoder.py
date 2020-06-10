from pathlib import Path
import json
class ObjectEncoder():
    def DecodificarDiccionario(self,d):
        from Clase_manejador import Manejador
        from Clase_nuevo import Nuevo
        from Clase_usado import Usado
        if "__class__" not in d:
            return d
        else:
            bandera=True
            class_name=d['__class__']
            class_=eval(class_name)
            if class_name=='Manejador':
                vehiculos=d['vehiculos']
                dAuto=vehiculos[0]
                manejador=class_()
                for i in range(len(vehiculos)):
                    dAuto=vehiculos[i]
                    class_name=dAuto.pop('__class__')
                    class_=eval(class_name)
                    atributos=dAuto['__atributos__']
                    if class_name=="Nuevo":
                        if bandera:
                            Nuevo.marca=atributos["marca"]
                            bandera=False
                        del(atributos["marca"])
                    vehiculo=class_(**atributos)
                    manejador.agregarEnLista(vehiculo)
                return manejador 
    def guardarEnArchivo(self,diccionario,archivo):
        with Path(archivo).open("w", encoding="UTF-8") as destino:
            json.dump(diccionario,destino,indent=4)
            destino.close()
    def leerArchivo(self,archivo):
        try:
            with Path(archivo).open(encoding="UTF-8") as fuente:
                diccionario=json.load(fuente)
                fuente.close()
        except:
            diccionario=-1
        return diccionario