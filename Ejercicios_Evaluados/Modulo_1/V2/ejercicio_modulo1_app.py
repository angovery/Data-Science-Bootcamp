# Archivo principal de la aplicación

import csv
import os
import ejercicio_modulo1_menus as menu
import ejercicio_modulo1_usuario_crud as crud

def leer_fichero_usuarios(fichero_csv):
    lista_usuarios = []
    print(f"Directorio de trabajo actual: {os.getcwd()}")
    try:
        with open(fichero_csv, mode = "r", encoding= "utf-8") as file:
            lineas = csv.reader(file)
            for linea in lineas:
                new_nombre = str(linea[0]).strip().lower()
                new_email = str(linea[1]).strip().lower()
                new_edad = int(linea[2].strip())
                new_altura = float(linea[3].strip())
                new_estudiante = str(linea[4]).strip().capitalize()
                usuario = crud.Usuario(new_nombre, new_email, new_edad, new_altura, new_estudiante)
                lista_usuarios.append(usuario)                
    except FileNotFoundError:
        print(f"\nNo se encuentra el archivo especificado: {fichero}\nPor favor, revise si existe el fichero en la ubicación del archivo ejecutable del programa y vuelva a ejecutar el programa.\n")
        exit()
    except Exception as e:
        print (f"\nSe ha producido un error inesperado: {e}\n")
    else:
        return lista_usuarios
        
        

fichero = '\Ejercicios_Evaluados\Modulo_1\V2\usuarios.csv'
lista = leer_fichero_usuarios(fichero)
#lista = crud.crear_lista_inicial()
#crud.imprimir_lista(lista)
crud.imprimir_menu(menu.opciones_menu_principal)

while True:
    option = crud.seleccionar_opcion(menu.opciones_menu_principal)
    match option:
        case 1: # Imprimir todos los usuarios de la lista.
            crud.imprimir_lista(lista)
            
        case 2: # Imprimir los usuarios ordenados por edad, ascendente o descendentemente.
            crud.imprimir_usuarios_ordenados_edad(lista, menu.opciones_submenu_lista_ordenada)
                
        case 3: # Buscar usuario por email
            crud.imprimir_usuario_por_email(lista)
                
        case 4: # Crea un nuevo usuario y se añade a la lista
            crud.crear_usuario(lista)
                            
        case 5: # Actualizar datos de un usuario existente. Dado que se utiliza el email como clave única, el email no puede modificarse. En caso de actualizarse el email, se deberá eliminar el usuario en cuestión y crear un nuevo usuario con los datos actualizados.
            crud.actualizar_usuario(lista)
        
        case 6: # Se elimina un usuario a partir de su email asociado.
            crud.eliminar_usuario(lista)

        case 7: # Se elimina la lista completa de usuarios.
            crud.eliminar_lista(lista)
        
        case 8:
            print ("\n", "Hasta pronto.", "\n")
            break

    crud.imprimir_menu(menu.opciones_menu_principal)