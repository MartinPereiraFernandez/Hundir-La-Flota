

from tablero import Tablero



class Juego:
    def __init__(self):
        self.obj_tablero = Tablero()
        self.lanzar_ataque(1, 1) #Con esto el usuario manda un ataque a la cordenada 1/1 en este caso hay una nave, por lo que se retornara tocado.
        self.lanzar_ataque(1,2)
        self.lanzar_ataque(1, 3)
        self.lanzar_ataque(1, 4)
        self.lanzar_ataque(1, 5)


    def inicializar_naves(self): #Otra función sin realizar, de verdad, debería cobrar más.
        pass

    def mostrar_resultado(self, resultado: int): #Los numeros asignados anteriormente permiten que ahora esas variables se intercambien por un printeo.
        if resultado == 0:
            print("Agua")
        elif resultado == 1:
            print("Tocado")
        elif resultado == 2:
            print("Hundido")

    def lanzar_ataque(self, x, y): #El usuario lanza el ataque
        print(f"Atacando a  {x}, {y} ")
        resultado = self.obj_tablero.comprobar_impacto(x, y)
        self.mostrar_resultado(resultado)




if __name__ == "__main__":
    Juego()