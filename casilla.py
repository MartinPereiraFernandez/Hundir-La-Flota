class Casilla:
    def __init__(self):
        self.nave = None
        self.visitada = False #Este iniciador hace que en un principio la casilla no este visitada, por lo que se pueda dispararle.

    def disparar(self):
        if self.visitada: #En el caso que la casilla este visitada se printeara un mensaje que le diga al usuario que ya se visitó esa casilla.
            print("Ya disparaste aquí")
            return None #El return none permite que en caso de haber una nave en esa casilla no se vuelva a tocar esa misma nave, es como si tocases agua.
        self.visitada = True #Esto hace que en todos los casos se visite la casilla y esta variable hace que no se pueda visitar otra vez.
        if self.nave is None: #En el caso de que en esa casilla no haya nada se retorna mensaje agua.
            print("Agua")
            return 0

        return self.nave.recibir_disparo()