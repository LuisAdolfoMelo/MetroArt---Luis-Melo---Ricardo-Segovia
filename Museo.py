










def menu():

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