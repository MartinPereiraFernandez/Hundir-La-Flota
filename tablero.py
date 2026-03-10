class Tablero:

    def __init__(self, tamano=10):
        self.AGUA = 0
        self.TOCADO = 1
        self.HUNDIDO = 2

    def colocar_nave(self, nave, x, y, orientacion):
        pass

    def comprobar_impacto(self, x, y):
        print("[LOG] estoy en tablero comprobando impacto")
        return self.AGUA