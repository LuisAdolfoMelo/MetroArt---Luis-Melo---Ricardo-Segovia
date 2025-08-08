import requests
from Clases import *
import random
from nacionalidades import lista_nacionalidades


class Museo:
    def __init__(self):
        pass


    def menu(self):

        while True:

            opcion_menu = input("""
    ---------------------------------------------------------------------
                                
                            -BIENVENIDO A METROART-
    QUE DESEA HACER: 
                                
                    [0] - CARGAR OBRAS DISPONIBLES
                    [1] - VER LISTA DE OBRAS POR DEPARTAMENTO 
                    [2] - VER LISTA DE OBRAS POR NACIONALIDAD DEL AUTOR
                    [3] - VER LISTA DE OBRAS POR NOMBRE DEL AUTOR 
                    [4] - MOSTRAR DETALLES DE OBRA 
                    [5] - SALIR 
                                
    ---------------------------------------------------------------------
    ------------> """)
            try: 
                opcion_menu = int(opcion_menu)

                if opcion_menu == 0:
                    self.mostrar_obras()
                elif opcion_menu == 1:
                   self.mostrar_obras_por_departamento()
                elif opcion_menu == 2:
                    self.mostrar_nacionalidades()
                    self.mostrar_obras_por_nacionalidad()
                elif opcion_menu == 3:
                    self.mostrar_obras_por_autor()

                elif opcion_menu == 4:
                    self.mostrar_obras_por_ID()

                elif opcion_menu == 5:
                    break
                else:
                    print("Opcion Invalida")
                    return


            except ValueError:
                print()
                print("Ingrese una opcion valida (1-2-3-4-5) ")
                
    def obtener_departamentos(self): #SIRVE

        """ Funcion para obtener los departamentos desde la API """

        url = "https://collectionapi.metmuseum.org/public/collection/v1/departments"
        resp = requests.get(url)
        return resp.json()["departments"]

    def mostrar_departamentos(self): #SIRVE
        """ Funcion para mostrar los departamentos y para volverlos objetos de tipo Departamento y 
        meterlos en una lista llamada self.obj_deptos """

        self.lista_deptos = self.obtener_departamentos()
        self.obj_deptos = [] #Lista de objetos Departamento
        for dept in self.lista_deptos:
            self.obj_deptos.append(Departamento(dept["departmentId"],dept["displayName"]))
        print("LOS DEPARTAMENTOS SON LOS SIGUIENTES: ")
        for depto in self.obj_deptos:
            depto.show()
    
    def obtener_obras(self): # SIRVE
        
        """ Funcion para obtener las obrass desde la API, se obtiene una muestra aleatorea de 5000 objetos"""

        url = "https://collectionapi.metmuseum.org/public/collection/v1/objects"

        resp = requests.get(url)
        ids = resp.json()["objectIDs"]
        return random.sample(ids,5000)
        # return ids
        
    def mostrar_obras_por_ID(self): #SRIVE 
        """Funcion para buscar obras por ID ingresado por el usuario"""
        
        id_obra = input("Ingrese el ID de la obra que desea buscar: ")
        try:
            id_obra = int(id_obra)

            print(f"Información de la obra con ID {id_obra}:")
            print()
            
            for obra in self.obj_obras:
                if obra.id == id_obra:
                    obra.show()
                else:
                    print(f"No se encontró ninguna obra con el ID {id_obra}.")


        except ValueError:
            print("Ingrese un ID válido (un número entero).")

    def obtener_info_obra(self,id_obra): #SIRVE
        """ Funcion para obtener la info de cada obra segun su ID"""

        url = f"https://collectionapi.metmuseum.org/public/collection/v1/objects/{id_obra}"
        resp = requests.get(url)
        return resp.json()
    
    def mostrar_obras(self): # SIRVE

        """ Funcion para mostrar las obras y volverlas objetos de tipo Obra y 
        meterlos en una lista llamada self.obj_obras """

        """ Lo limite a 20 nada mas porque si no el programa literalmente no corre y manda de una vez al try except del menu """

        lista_ids = self.obtener_obras()
        self.obj_obras = [] #Lista de objetos Obra
        limite = 20
        data_objetos = []

        for obj_id in lista_ids[:limite]:
            info_obra = self.obtener_info_obra(obj_id)

            # Extraer info relevantes
            
            datos_filtrados = {
                "id" : info_obra.get("objectID"),
                "titulo" : info_obra.get("title"),
                "nombre_artista" : info_obra.get("artistDisplayName"),
                "nacionalidad_artista" : info_obra.get("artistNationality"),
                "fecha_nacimiento_artista" : info_obra.get("artistBeginDate"),
                "fecha_muerte_artista" : info_obra.get("artistEndDate"),
                "tipo" : info_obra.get("classification"),
                "año_creacion" : info_obra.get("objectDate"),
                "imagen_URL" : info_obra.get("primaryImage"),
                "departamento" : info_obra.get("department")
            }
            data_objetos.append(datos_filtrados)

        for obra_data in data_objetos:
            self.obj_obras.append(Obra(obra_data["id"], obra_data["titulo"], obra_data["nombre_artista"],obra_data["nacionalidad_artista"], obra_data["fecha_nacimiento_artista"],obra_data["fecha_muerte_artista"],obra_data["tipo"],obra_data["año_creacion"],obra_data["imagen_URL"],obra_data["departamento"]))
            
        print("LAS OBRAS SON LAS SIGUIENTES: ")
        for obra in self.obj_obras:
            obra.show()
        
    def mostrar_obras_por_departamento(self): #SIRVE
        """Funcion para mostrar las obras por departamento ingresado por el usuario"""
        self.mostrar_departamentos()
        id_depto = int(input("Ingrese el ID del departamento que desea ver: "))
        
        #Encontrar el departamento por el id ingreesado por el usuario
        nombre_depto = None
        for depto in self.obj_deptos:
            if depto.id == id_depto:
                nombre_depto = depto.nombre_departamento
                break
        
        if not nombre_depto:
            print("No existe un departamento con ese ID.")
            return
      
        print()
        print("LAS OBRAS DEL DEPARTAMENTO SELECCIONADO SON LAS SIGUIENTES: ")
        print()
        for obra in self.obj_obras:
            if obra.departamento == nombre_depto:
                obra.show()
        
    def mostrar_nacionalidades(self): #SIRVE
        """Se muestran las nacionalidades en una lista enumerada """
        print("Nacionalidades: ")
        print()
        for numero, nacionalidad in enumerate(lista_nacionalidades): #enumerate para ponerle un indice a la nacionalidad y que el usuario no tenga que escribir , solo poner el numero
            print(f"[{numero+1}] - {nacionalidad}") # le sumamos para eliminar el 0 de la lista

    def mostrar_obras_por_nacionalidad(self): # SIRVE
        """Se imprimen las obras por la nacionalidad ingresada por el usuario"""
    
        nacionalidad_deseada = input("Indique el ID de la nacionalidad para ver obras: ")
        try: 
            nacionalidad_deseada = int(nacionalidad_deseada)
                   
            if 1 <= nacionalidad_deseada <= len(lista_nacionalidades): # condicional que revisa que el input este dentro de los parametros de la lista de nacionalidades enumerada
                nacionalidad_seleccionada = lista_nacionalidades[nacionalidad_deseada - 1] # restamos 1 para que coincida con el indice de la lista 
                print()
                print(f"Obras de artistas de nacionalidad {nacionalidad_seleccionada}:")
                print()
                for obra in self.obj_obras:
                    if obra.nacionalidad_artista == nacionalidad_seleccionada:
                        obra.show()
            else:
                print("ID de nacionalidad inválido.")

        except ValueError:
            print("Ingrese el numero indicado en la lista de nacionalidades porfavor ")


    def mostrar_obras_por_autor(self): #NO SIRVE ?? 
        """Funcion para mostrar las obras por nombre de autor ingresado por el usuario"""
        
        nombre_autor = input("Ingrese el nombre del autor que desea buscar: ")
        try:
            # nombre_autor = str(nombre_autor)
            # nombre_autor = nombre_autor.title()

            print(f"Obras del autor {nombre_autor}:")
            print()
            
            for obra in self.obj_obras:
                if obra.nombre_artista == nombre_autor:
                    obra.show()
                else:
                    print("Autor no detectado")
                    return
        except ValueError:
            print("Ingrese un nombre: ")
