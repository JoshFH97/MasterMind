from colored import fg, attr
class Tablero:
    colores = {#crear el dicionario para reutilizar los colores.
        'r': fg(1),
        'g': fg(2),
        'y': fg(3),
        'b': fg(4),
    }

    def __init__(self) -> None:
        self.color_secreto = []
        self.turnos = []
    
    def crear_color(self, color):#indica el codigo.
        self.color_secreto = color

    def validar_ganador(self, intento):#Indica el panel para ver lal pistas.
        retroalimentacion = []
        copia_color = self.color_secreto.copy()
        for i in range (4):
            
            if intento[i] == copia_color[i]:
                retroalimentacion.append('verde')
                copia_color[i] = None
            elif intento[i] in copia_color:
                retroalimentacion.append('amarillo')
                copia_color.remove(intento[i])
            else:
                retroalimentacion.append('blanco')
        return retroalimentacion

    def mostrar(self): #muestra los colores en el panel.
        for intento, retroalimentacion in self.turnos:
            fila_jugada = ' '.join([self.colores[color]+"o"+attr('reset') for color in intento])

            retro_jugada = ' '.join([
            fg(2) + 'o'+ attr('reset') if adivina == 'verde'
            else fg(3)+'o'+attr('reset') if adivina == 'amarillo'
            else '○'
            
            for adivina in retroalimentacion
        ])
        print(f'{fila_jugada}|{retro_jugada}')
    
    def actualizar_tablero(self, intento, retroalimentacion):
        self.turnos.append((intento, retroalimentacion))