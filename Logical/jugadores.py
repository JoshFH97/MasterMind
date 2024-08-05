import random

# Lista de colores posibles
colores = ['r', 'b', 'y', 'g']

# Tamaño del código a adivinar o crear
tamano_code = 4

# Clase base para un jugador
class Jugador:

    def __init__(self, persona):
        # Inicializa un jugador, indicando si es una persona o no
        self.persona = persona

# Clase para un jugador que adivina el código
class Adivinador(Jugador):
    def obtener_codigo(self):
        if self.persona:
            # Si el jugador es una persona, se pide que introduzca un código de 4 colores
            codigo = input('Inserte el código de 4 colores de la siguiente manera (r, b, g, y): ').strip().split()
            # Se convierte la entrada en una lista de colores
            return codigo
        else:
            # Si el jugador no es una persona, se genera un código aleatorio de 4 colores
            return random.choices(colores, k=tamano_code)

# Clase para un jugador que crea el código
class Creador(Jugador):
    def obtener_codigo(self):
        if self.persona:
            # Si el jugador es una persona, se pide que introduzca un código de 4 colores
            codigo = input('Inserte el código de 4 colores de la siguiente manera (r, b, g, y): ').strip().split()
            # Se convierte la entrada en una lista de colores
            return codigo
        else:
            # Si el jugador no es una persona, se genera un código aleatorio de 4 colores
            return random.choices(colores, k=tamano_code)

# # Ejemplo de uso:
# # Crear un adivinador que es una persona
# jugador1 = Adivinador(persona=True)
# # Obtener el código del adivinador
# codigo_adivinador = jugador1.obtener_codigo()
# # Imprimir el código
# print(codigo_adivinador)

# # Crear un creador que no es una persona
# jugador2 = Creador(persona=False)
# # Obtener el código del creador
# codigo_creador = jugador2.obtener_codigo()
# # Imprimir el código
# print(codigo_creador)
