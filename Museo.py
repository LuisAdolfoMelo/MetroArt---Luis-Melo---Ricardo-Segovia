import requests
from Clases import *
import random



class Museo:
    def __init__(self):
        pass


    def menu(self):

        while True:

            opcion_menu = input("""
    ---------------------------------------------------------------------
                                
                            -BIENVENIDO A METROART-
    QUE DESEA HACER: 
                    [1] - VER LISTA DE OBRAS POR DEPARTAMENTO 
                    [2] - VER LISTA DE OBRAS POR NACIONALIDAD DEL AUTOR
                    [3] - VER LISTA DE OBRAS POR NOMBRE DEL AUTOR 
                    [4] - MOSTRAR DETALLES DE OBRA 
                    [5] - SALIR 
                                
    ---------------------------------------------------------------------
    ------------> """)
            try: 
                opcion_menu = int(opcion_menu)

                if opcion_menu == 1:
                    # self.mostrar_departamentos()
                    # self.mostrar_obras()
                    self.mostrar_obras_por_departamento()
                elif opcion_menu == 2:
                    pass

                elif opcion_menu == 3:
                    pass

                elif opcion_menu == 4:
                    pass

                elif opcion_menu == 5:
                    break
                else:
                    print("Opcion Invalida")


            except ValueError:
                print()
                print("Ingrese una opcion valida (1-2-3-4-5) ")
                
    def obtener_departamentos(self):

        """ Funcion para obtener los departamentos desde la API """

        url = "https://collectionapi.metmuseum.org/public/collection/v1/departments"
        resp = requests.get(url)
        return resp.json()["departments"]

    def mostrar_departamentos(self):
        """ Funcion para mostrar los departamentos y para volverlos objetos de tipo Departamento y 
        meterlos en una lista llamada self.obj_deptos """

        self.lista_deptos = self.obtener_departamentos()
        self.obj_deptos = []
        for dept in self.lista_deptos:
            self.obj_deptos.append(Departamento(dept["departmentId"],dept["displayName"]))
        print("LOS DEPARTAMENTOS SON LOS SIGUIENTES: ")
        for depto in self.obj_deptos:
            depto.show()
    
    def obtener_obras(self):
        
        """ Funcion para obtener las obrass desde la API"""

        url = "https://collectionapi.metmuseum.org/public/collection/v1/objects"

        resp = requests.get(url)
        ids = resp.json()["objectIDs"]
        return random.sample(ids, 100)
        
    def obtener_info_obra(self,id_obra):
        """ Funcion para obtener la info de cada obra segun su ID"""

        url = f"https://collectionapi.metmuseum.org/public/collection/v1/objects/{id_obra}"
        resp = requests.get(url)
        return resp.json()
    
    def mostrar_obras(self):

        """ Funcion para mostrar las obras y para volverlas objetos de tipo Obra y 
        meterlos en una lista llamada self.obj_obras """

        lista_ids = self.obtener_obras()
        self.obj_obras = []

        for id in lista_ids:
            try:
                info_obra = self.obtener_info_obra(id)
                self.obj_obras.append(Obra(info_obra["objectID"],info_obra["title"],info_obra["artistDisplayName"],info_obra["department"],info_obra["culture"],info_obra["objectURL"]))
            except:
                pass
        print("LAS OBRAS SON LAS SIGUIENTES: ")
        for obra in self.obj_obras:
            obra.show()
        
    def mostrar_obras_por_departamento(self):
        """Funcion para mostrar las obras por departamento"""
        self.mostrar_departamentos()
        id_depto = int(input("Ingrese el ID del departamento que desea ver: "))
        lista_ids = self.obtener_obras()
        self.obj_obras = []
        for id in lista_ids:
            info_obra = self.obtener_info_obra(id)
            if "departmentId" in info_obra and info_obra["departmentId"] == id_depto:
                self.obj_obras.append(Obra(info_obra["objectID"],info_obra["title"],info_obra["artistDisplayName"],info_obra["department"],info_obra["culture"],info_obra["objectURL"]))

        print("LAS OBRAS DEL DEPARTAMENTO SELECCIONADO SON LAS SIGUIENTES: ")
        for obra in self.obj_obras:
            obra.show()
        
       

       

     