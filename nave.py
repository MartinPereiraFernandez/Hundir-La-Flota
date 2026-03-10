from juego import Juego
from tablero import Tablero
class Nave:
    def __init__(self, nombre,tipo,vida):
        self.nombre=nombre
        self.tipo=tipo
        self.vida=vida

    def recibirDisparo(self):
        self.vida = self.vida-1










