import random

class Mastermind:
    def __init__(self, colores, max_intentos, tamano_code):
        self.colores = colores
        self.max_intentos = max_intentos
        self.tamano_code = tamano_code
        self.code = random.choices(self.colores, k=self.tamano_code)
        self.attempts = 0

    def mostrar_codigo(self):
        return self.code

    def hacer_intento(self, intento):
        if len(intento) != self.tamano_code:
            return "El intento debe tener el tamaño correcto de código."
        self.attempts += 1
        return self._comparar_codigos(intento)

    def _comparar_codigos(self, intento):
        correctos = sum(1 for i, color in enumerate(intento) if color == self.code[i])
        mal_posicionados = sum(1 for color in intento if color in self.code) - correctos
        return {
            "correctos": correctos,
            "mal_posicionados": mal_posicionados,
            "intentos_restantes": self.max_intentos - self.attempts
        }

    def juego_terminado(self):
        return self.attempts >= self.max_intentos

# Ejemplo de uso de la clase Mastermind
colores = ['red', 'blue', 'green', 'yellow']
max_intentos = 12
tamano_code = 4

juego = Mastermind(colores, max_intentos, tamano_code)
print("Código secreto:", juego.mostrar_codigo())

intento = ['red', 'blue', 'green', 'yellow']
resultado = juego.hacer_intento(intento)
print("Resultado del intento:", resultado)
print("¿Juego terminado?", juego.juego_terminado())
