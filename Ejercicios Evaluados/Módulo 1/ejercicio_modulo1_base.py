# Ejercicio Nº1 - Módulo 1

class Usuario:
# Declaración de la clase Usuario
    
    # Constructor de la clase Usuario
    def __init__(self, nombre, email, edad, altura, estudiante, cumpleanos):
        self.nombre = nombre # Tipo str
        self.email = email # Tipo str
        self.edad = edad # Tipo int
        self. altura = altura # Tipo float
        self.estudiante = estudiante # Tipo bool
        # self.cumpleanos = cumpleanos # Tipo date
        
    # Método para imprimir el objeto
    def __str__(self):
        return f"Nombre: {self.nombre},
                Email: {self.email},
                Edad: {self.edad},
                Altura: {self.altura}
                Estudiante: {self.estudiante}
                "
    