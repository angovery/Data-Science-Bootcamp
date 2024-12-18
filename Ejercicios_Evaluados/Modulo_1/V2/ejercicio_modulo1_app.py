# Archivo principal de la aplicación

import ejercicio_modulo1_menus as menu
import ejercicio_modulo1_usuario_crud as crud
import ejercicio_modulo1_ficheros as file
     

fichero = './Ejercicios_Evaluados/Modulo_1/V2/usuarios.csv'
lista = file.leer_fichero_usuarios(fichero)

while True:
    crud.imprimir_menu(menu.opciones_menu_principal)
    option = crud.seleccionar_opcion(menu.opciones_menu_principal)
    match option:
        case 1: # Imprimir todos los usuarios de la lista.
            crud.imprimir_lista(lista)
            
        case 2: # Imprimir los usuarios ordenados por edad, ascendente o descendentemente.
            crud.imprimir_usuarios_ordenados_edad(lista, menu.opciones_submenu_lista_ordenada)
                
        case 3: # Buscar usuario por email
            crud.imprimir_usuario_por_email(lista)
                
        case 4: # Crea un nuevo usuario y se añade a la lista
            crud.crear_usuario(lista, fichero)
                                        
        case 5: # Actualizar datos de un usuario existente. Dado que se utiliza el email como clave única, el email no puede modificarse. En caso de actualizarse el email, se deberá eliminar el usuario en cuestión y crear un nuevo usuario con los datos actualizados.
            crud.actualizar_usuario(lista)
        
        case 6: # Se elimina un usuario a partir de su email asociado.
            crud.eliminar_usuario(lista)

        case 7: # Se elimina la lista completa de usuarios.
            crud.eliminar_lista(lista)
        
        case 8:
            file.actualizar_fichero(fichero,lista) # En tiempo de ejecución, la lista de usuarios se puede haber modificado o eliminado algún elemento. Este paso sobreescribe en el fichero csv la lista actualizda de usuarios. Este paso, podría sustituir a la adicción en el fichero de un nuevo usuario del caso 5.
            print ("\n", "Hasta pronto.", "\n")
            break