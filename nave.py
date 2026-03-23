class Nave:
    def __init__(self, nombre, tipo, vida):
        self.nombre=nombre
        self.tipo=tipo
        self.vida=vida

    def recibir_disparo(self):
        self.vida = self.vida-1
        print("Tocado")
        if self.vida==0:
            print("Hundido")







