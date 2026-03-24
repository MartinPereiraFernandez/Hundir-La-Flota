class Nave:
    def __init__(self, nombre, tipo, vida):#Atributos a las naves para que se identifique a cada nave con su nombre, tipo y vida.
        self.nombre=nombre
        self.tipo=tipo
        self.vida=vida#La vida de la nave dependerá unicamente de su tipo.

    def recibir_disparo(self):#La funcion recibir disparo descontará una vida a la nave
        self.vida = self.vida-1
        print("Tocado")#Al recibir un disparo el juego recibirá un tocado ya que se tocó una nave.
        if self.vida==0:#Este caso para cuando una nave se queda sin vidas se hundirá por lo que esa nave deja se existir y se printeará hundido.
            print("Hundido")







