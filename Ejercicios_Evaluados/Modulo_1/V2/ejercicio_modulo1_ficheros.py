# Módulo con funciones de tratamiento de ficheros con elementos de usuarios.

import csv
import ejercicio_modulo1_usuario as user

def leer_fichero_usuarios(fichero_csv):
    lista_usuarios = []
    #print(f"Directorio de trabajo actual: {os.getcwd()}")
    try:
        with open(fichero_csv, mode = "r", encoding= "utf-8") as file:
            lineas = csv.reader(file)
            for linea in lineas:
                new_nombre = str(linea[0]).strip().lower()
                new_email = str(linea[1]).strip().lower()
                new_edad = int(linea[2].strip())
                new_altura = float(linea[3].strip())
                new_estudiante = str(linea[4]).strip().capitalize()
                usuario = user.Usuario(new_nombre, new_email, new_edad, new_altura, new_estudiante)
                lista_usuarios.append(usuario)                
    except FileNotFoundError:
        print(f"\nNo se encuentra el archivo especificado: {fichero_csv}\nPor favor, revise si existe el fichero en la ubicación del archivo ejecutable del programa y vuelva a ejecutar el programa.\n")
        exit()
    except Exception as e:
        print (f"\nSe ha producido un error inesperado: {e}\n")
    else:
        return lista_usuarios
    
def incluir_usuario_fichero (fichero_csv, usuario):
    try:
        with open(fichero_csv, mode = "w", encoding= "utf-8") as file:
                new_nombre = str(usuario.nombre).strip().lower()
                new_email = str(usuario.email).strip().lower()
                new_edad = str(usuario.edad).strip().lower()
                new_altura = str(usuario.altura).strip().lower()
                new_estudiante = str(usuario.estudiante).strip().lower()
                linea = new_nombre + ", " + new_email + ", " + new_edad + ", " + new_altura + ", " + new_estudiante
                print(linea)
                
                            
    except FileNotFoundError:
        print(f"\nNo se encuentra el archivo especificado: {fichero_csv}\nPor favor, revise si existe el fichero en la ubicación del archivo ejecutable del programa y vuelva a ejecutar el programa.\n")
        exit()
    except Exception as e:
        print (f"\nSe ha producido un error inesperado: {e}\n")
