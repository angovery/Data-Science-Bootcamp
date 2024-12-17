# Archivo de definición de menús de la aplicación.

""" Se crean las opciones del menú principal en una tupla (ya que, en principio, no se van a alterar los elementos del menú).
Si es preciso, para facilitar el mantenimiento, y por si posteriormente se desea añadir, modificar o eliminar alguna,
se puede modificar la tupla a nivel de código. El primer elemento de la lista es el título del menú.
"""
opciones_menu_principal = (
        "\n-----MENU DE PRINCIPAL-----\n",
        "1 - Imprimir todos los usuarios de la lista",
        "2 - Imprimir todos los usuarios ordenados por edad",
        "3 - Imprimir un usuario por su email",
        "4 - Crear un nuevo usuario",
        "5 - Actualizar un usuario existente",
        "6 - Borrar usuario por su email",
        "7 - Borrar todos los usuarios",
        "8 - Salir"
    )

# Opciones posibles del submenú de la opción 2 del menú principal, Imprimir lista ordenada
opciones_submenu_lista_ordenada = (
    "\n-----OPCIONES DE ORDENACIÓN-----\n",
    "1 - Ascendente",
    "2 - Descendente",
    "3 - Volver al Menú Principal",
    "4 - Salir"
)

# Opciones posibles del submenú de la opción 7 del menú principal, Eliminar la lista completa
opciones_submenu_eliminar_lista = (
    "\n-----OPCIONES DE ELIMINACIÓN DE LISTA-----\n",
    "1 - Sí, eliminar la lista completa.",
    "2 - No. Mantener la lista completa y volver al Menú Principal",
    "3 - Salir"
)