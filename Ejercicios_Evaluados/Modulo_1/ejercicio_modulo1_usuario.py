# Archivo de definición de la clase Usuarios y varios métodos asociados

class Usuario:
# Declaración de la clase Usuario
    
    # Constructor de la clase Usuario
    def __init__(self, nombre, email, fecha_nacimiento, edad, altura, estudiante):
        self.nombre = nombre # Tipo str
        self.email = email # Tipo str
        self.fecha_nacimiento = fecha_nacimiento # Tipo date
        self.edad = edad # Tipo int
        self.altura = altura # Tipo float
        self.estudiante = estudiante # Tipo bool
        
    # Método para imprimir el objeto
    def __str__(self):
        return f"Nombre: {self.nombre}, Email: {self.email}, Cumpleaños: {self.fecha_nacimiento}, Edad: {self.edad}, Altura: {self.altura}, Estudiante: {self.estudiante}"