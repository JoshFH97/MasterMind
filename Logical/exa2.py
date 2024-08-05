import random

class Mastermind:
    def __init__(self, colores, max_intentos, tamano_code):
        self.colores = colores
        self.max_intentos = max_intentos
        self.tamano_code = tamano_code
        self.code = random.choices(self.colores, k=self.tamano_code)
        self.attempts = 0

# Ejemplo de uso de la clase Mastermind
colores = ['red', 'blue', 'green', 'yellow']
max_intentos = 12
tamano_code = 4

juego = Mastermind(colores, max_intentos, tamano_code)
print("Código secreto:", juego.code)  # Solo para mostrar el código generado

