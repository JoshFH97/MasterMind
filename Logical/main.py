from jugadores import Adivinador, Creador
from tablero import Tablero

# Definición de la clase Turno
class Turno:
    # Constructor de la clase Turno
    def __init__(self) -> None:
        self.tablero = Tablero()  # Inicializa un objeto Tablero
        self.crear_codigo = None  # Inicializa el atributo crear_codigo en None
        self.adivinar_codigo = None  # Inicializa el atributo adivinar_codigo en None

    # Método para configurar los jugadores
    def operador(self):
        # Solicita al usuario que elija ser creador o adivinador
        jugador1_input = input('Quieres ser el creador(0) o el adivinador(1)? Indique numero:')
        
        if jugador1_input == '1':
            # Si elige 1, el usuario es el adivinador y la máquina es el creador
            self.adivinar_codigo = Adivinador(persona=True)
            self.crear_codigo = Creador(persona=False)
        elif jugador1_input == '0':
            # Si elige 0, el usuario es el creador y la máquina es el adivinador
            self.adivinar_codigo = Adivinador(persona=False)
            self.crear_codigo = Creador(persona=True)
        else:
            # Si ingresa un valor no válido, muestra un mensaje y termina el método
            print('No se reconoce caracter.')
            return

        # Se crea el código de colores usando el método del creador
        self.tablero.crear_color(self.crear_codigo.obtener_codigo())

    # Método para jugar el juego
    def juego(self):
        # Verifica que los jugadores estén configurados antes de iniciar el juego
        if self.crear_codigo is None or self.adivinar_codigo is None:
            print("Primero se debe configurar el juego llamando al método 'operador'.")
            return

        # Bucle de hasta 12 intentos para adivinar el código
        for i in range(12):
            # El adivinador obtiene un intento de código
            intento = self.adivinar_codigo.obtener_codigo()
            # Valida si el intento es el código correcto
            retroalimentacion = self.tablero.validar_ganador(intento)
            # Actualiza el tablero con la retroalimentación obtenida
            self.tablero.actualizar_tablero(intento,retroalimentacion)
            self.tablero.mostrar()
            print(f"turno {i}")
            if retroalimentacion == ["verde"] * 4:
                # Si el intento es correcto, muestra mensaje de victoria y termina el bucle
                print("¡Felicidades! Has ganado el juego.")
                break
            # Si se alcanzan los 12 intentos sin acertar, muestra mensaje de derrota
            print("Lo siento, has perdido el juego.")

        
if __name__ == "__main__":
    turno = Turno()
    turno.operador()
    turno.juego()
