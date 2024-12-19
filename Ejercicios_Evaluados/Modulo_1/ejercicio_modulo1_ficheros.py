# Módulo con funciones de tratamiento de ficheros con elementos de usuarios.

from datetime import datetime, date
import csv
import ejercicio_modulo1_usuario as user
import ejercicio_modulo1_usuario_crud as crud

# Función que toma una fecha (de cumpleaños) en formato DD/MM/AAAA, de tipo string. Devuelve la edad actual, de tipo int.
def calcular_edad_actual(fecha_cumple):
    fecha = datetime.strptime(fecha_cumple, "%d/%m/%Y").date()
    fecha_actual = date.today()
    diferencia = fecha_actual - fecha
    diferencia_en_anos = int(diferencia.days / 365)
    return diferencia_en_anos
    

# Función que se encarga de leer los datos de un archivo externo csv, que contiene datos de un objeto de tipo Usuario. Devuelve una lista cuyos elementos son objetos de tipo Usuario.
def leer_fichero_usuarios(fichero_csv):
    lista_usuarios = []
    try:
        with open(fichero_csv, mode = "r", encoding= "utf-8") as file:
            lineas = csv.reader(file)
            for linea in lineas:
                new_nombre = str(linea[0]).strip().lower()
                new_email = str(linea[1]).strip().lower()
                new_fecha_nacimiento = str(linea[2]).strip()
                new_edad = calcular_edad_actual(new_fecha_nacimiento) # La edad se calcula en base a la fecha de nacimiento.
                new_altura = float(linea[4].strip())
                new_estudiante = str(linea[5]).strip().capitalize()
                usuario = user.Usuario(new_nombre, new_email, new_fecha_nacimiento, new_edad, new_altura, new_estudiante)
                lista_usuarios.append(usuario)                
    except FileNotFoundError:
        print(f"\nNo se encuentra el archivo especificado: {fichero_csv}\nPor favor, revise si existe el fichero en la ubicación del archivo ejecutable del programa y vuelva a ejecutar el programa.\n")
        exit()
    except Exception as e:
        print (f"\nSe ha producido un error inesperado: {e}\n")
    else:
        return lista_usuarios
    
# Función que toma como entrada el nombre de un fichero csv, que debe existir, con datos de tipo usuario y un objeto de tipo usuario. La función añade los datos del usuario al final del archivo dado.
def incluir_usuario_fichero (fichero_csv, usuario):
    try:
        with open(fichero_csv, mode = "a", newline = '\n', encoding= "utf-8") as file:
            linea = csv.writer(file)
            lista = []
            new_nombre = str(usuario.nombre).strip().lower()
            lista.append(new_nombre)
            new_email = str(usuario.email).strip().lower()
            lista.append(new_email)
            new_date = str(usuario.fecha_nacimiento).strip().lower()
            lista.append(new_date)
            new_edad = str(calcular_edad_actual(new_date)).strip()
            lista.append(new_edad)
            new_altura = str(usuario.altura).strip().lower()
            lista.append(new_altura)
            new_estudiante = str(usuario.estudiante).strip().lower()
            lista.append(new_estudiante)
            print(lista)
            linea.writerow(lista)                                      
    except FileNotFoundError:
        print(f"\nNo se encuentra el archivo especificado: {fichero_csv}\nPor favor, revise si existe el fichero en la ubicación del archivo ejecutable del programa y vuelva a ejecutar el programa.\n")
        exit()
    except Exception as e:
        print (f"\nSe ha producido un error inesperado: {e}\n")
    else:
        print("\nUsuario añadido al fichero correctamente.\n")

# Función que toma como entrada el nombre de un fichero csv, que debe existir, con datos de tipo usuario y una lista de elementos de tipo usuario. La función sobreescribe los datos del archivo dado con los datos de usuarios de la lista.
def actualizar_fichero (fichero_csv, lista_usuarios):
    try:
        with open(fichero_csv, mode = "w", newline = '\n', encoding= "utf-8") as file:
            escribe_lista = csv.writer(file)
            for usuario in lista_usuarios:
                escribe_lista.writerow([usuario.nombre, usuario.email, usuario.fecha_nacimiento, usuario.edad, usuario.altura, usuario.estudiante])    
    except FileNotFoundError:
        print(f"\nNo se encuentra el archivo especificado: {fichero_csv}\nPor favor, revise si existe el fichero en la ubicación del archivo ejecutable del programa y vuelva a ejecutar el programa.\n")
        exit()
    except Exception as e:
        print (f"\nSe ha producido un error inesperado al actualizar el fichero de usuarios: {e}\n")
    else:
        print("\nFichero actualizado correctamente.\n")
        