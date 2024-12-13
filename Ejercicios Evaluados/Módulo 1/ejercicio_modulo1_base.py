# Ejercicio Nº1 - Módulo 1

class Usuario:
# Declaración de la clase Usuario
    
    # Constructor de la clase Usuario
    def __init__(self, nombre, email, edad, altura, estudiante):
        self.nombre = nombre # Tipo str
        self.email = email # Tipo str
        self.edad = edad # Tipo int
        self. altura = altura # Tipo float
        self.estudiante = estudiante # Tipo bool
        # self.cumpleanos = cumpleanos # Tipo date
        
    # Método para imprimir el objeto
    def __str__(self):
        return f"Nombre: {self.nombre}, Email: {self.email}, Edad: {self.edad}, Altura: {self.altura}, Estudiante: {self.estudiante}"
               
# Función para imprimir un menú
def imprimir_menu():
    opciones_menu = (
        "1 - Imprimir todos los usuarios de la lista",
        "2 - Imprimir todos los usuarios ordenados por edad",
        "3 - Imprimir un usuario por su email",
        "4 - Crear un nuevo usuario",
        "5 - Actualizar un usuario existente",
        "6 - Borrar usuario por su email",
        "7 - Borrar todos los usuarios",
        "8 - Salir"
    ) # Se crean las opciones en una tupla (ya que, en principio, no se van a alterar los elementos del menú). Si es preciso, para facilitar el mantenimiento, y por si posteriormente se desea añadir, modificar o eliminar alguna, se puede modificar la tupla a nivel de código.
    print("-----MENU DE PRINCIPAL-----")
    for opcion in opciones_menu:
        print(opcion)
    print("\n", "\n")

# Función para el tratamiento de la opción seleccionada
def seleccionar_opcion():
    opcion = input("Por favor, seleccione una de las opciones indicadas arriba, tecleando el número correspondiente y pulsando 'Enter': ")
 
# Función para crear ina lista de usuarios inicial
def crear_lista_inicial():   
    # Se definen los usuarios de base.
    user1 = Usuario("Jose", "jose@nttdata.com", 49, 1.83, True)
    user2 = Usuario("Juan", "juan@nttdata.com", 39, 1.95, True)
    user3 = Usuario("Aaron", "aaron@google.com", 26, 1.74, False)
    user4 = Usuario("Borja", "borja@microsoft.com", 51, 1.67, False)

    # Se crea una lista de usuarios.
    usuarios = [user1, user2, user3, user4]
    return usuarios

"""
usuarios = [
    Usuario("Jose", "jose@nttdata.com", "49", "1.83", True)
    Usuario("Juan", "juan@nttdata.com", "39", "1.95", True)
    Usuario("Aaron", "aaron@google.com", "26", "1.74", False)
    Usuario("Borja", "borjae@microsoft.com", "51", "1.67", False)    
]
"""
# Función para imprimir una lista cuyos elementos son de tipo Usuario (valdría igualmente cualquier tipo de elemento).
def imprimir_lista(lista):
    if not lista:
        print("Lista vacía. No se puede imprimir")
    else:
        for elemento_lista in lista:
            print(elemento_lista)
    print("\n")

# Función para ordenar una lista, en base a una clave, ya sea de forma ascendente o descendente
# def ordenar_lista(lista, clave, orden):
    

# ---------- BLOQUE PRINCIPAL DEL PROGRAMA ----------

lista = crear_lista_inicial()
imprimir_lista(lista)
imprimir_menu()
seleccionar_opcion()


    


