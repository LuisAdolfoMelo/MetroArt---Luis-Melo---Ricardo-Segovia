import requests
from Clases import *


class Museo:
    def __init__(self):
        pass


    def obtener_departamentos(self):
        """
        Obtiene la lista de departamentos del Met Museum (ID y nombre) sin manejo de errores.
        Retorna lista de tuplas (ID, nombre) o lista vacía si falla silenciosamente.
        """
        url = "https://collectionapi.metmuseum.org/public/collection/v1/departments"
        resp = requests.get(url)
        data = resp.json()
        return [(depto["departmentId"], depto["displayName"]) for depto in data.get("departments", [])]



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
                    pass

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