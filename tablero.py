
from casilla import Casilla
from nave import Nave

class Tablero:

    def __init__(self, tamano=10): #Este init le da numeros a las respuestas para que retorne agua, tocado o hundido.
        self.agua = 0
        self.tocado = 1
        self.hundido = 2

        por1=Nave("Enterprise","portaaviones",5) #Se les da forma a todas las naves creadas para luego meterlas dentro del tablero.

        fra1=Nave("Bismarck","fragata",3)
        fra2=Nave("Prince of Wales","fragata",3)
        fra3=Nave("Graf Spee","fragata",3)

        sub1 = Nave("U-47", "submarino", 1)
        sub2 = Nave("U-96", "submarino", 1)
        sub3 = Nave("U-505", "submarino", 1)
        sub4 = Nave("U-534", "submarino", 1)

        print(por1.nombre)

        self.casillero = [
            [Casilla(), Casilla(), Casilla(), Casilla(), Casilla(), Casilla(), Casilla(), Casilla(), Casilla(),
             Casilla()],

            [Casilla(), Casilla(), Casilla(), Casilla(), Casilla(), Casilla(), Casilla(), Casilla(), Casilla(),
             Casilla()],

            [Casilla(), Casilla(), Casilla(), Casilla(), Casilla(), Casilla(), Casilla(), Casilla(), Casilla(),
             Casilla()],

            [Casilla(), Casilla(), Casilla(), Casilla(), Casilla(), Casilla(), Casilla(), Casilla(), Casilla(),
             Casilla()],

            [Casilla(), Casilla(), Casilla(), Casilla(), Casilla(), Casilla(), Casilla(), Casilla(), Casilla(),
             Casilla()],

            [Casilla(), Casilla(), Casilla(), Casilla(), Casilla(), Casilla(), Casilla(), Casilla(), Casilla(),
             Casilla()],

            [Casilla(), Casilla(), Casilla(), Casilla(), Casilla(), Casilla(), Casilla(), Casilla(), Casilla(),
             Casilla()],

            [Casilla(), Casilla(), Casilla(), Casilla(), Casilla(), Casilla(), Casilla(), Casilla(), Casilla(),
             Casilla()],

            [Casilla(), Casilla(), Casilla(), Casilla(), Casilla(), Casilla(), Casilla(), Casilla(), Casilla(),
             Casilla()],

            [Casilla(), Casilla(), Casilla(), Casilla(), Casilla(), Casilla(), Casilla(), Casilla(), Casilla(),
             Casilla()]
        ]
        #Todas estas funciones repetitivas asignan los barcos a sus respectivas casillas.
        self.casillero[1][1].nave = por1
        self.casillero[1][2].nave = por1
        self.casillero[1][3].nave = por1
        self.casillero[1][4].nave = por1
        self.casillero[1][5].nave = por1


        self.casillero[3][3].nave = fra1
        self.casillero[4][3].nave = fra1
        self.casillero[5][3].nave = fra1

        self.casillero[7][1].nave = fra2
        self.casillero[7][2].nave = fra2
        self.casillero[7][3].nave = fra2

        self.casillero[9][1].nave = fra3
        self.casillero[9][2].nave = fra3
        self.casillero[9][3].nave = fra3


        self.casillero[4][6].nave = sub1
        self.casillero[9][9].nave = sub2
        self.casillero[7][6].nave = sub3
        self.casillero[9][5].nave = sub4

    def colocar_nave(self,nave,x,y,orientacion): #Funcion creada pero que aun no está funcional, tienen que darme mas presupuesto para que la haga.
        pass

    def comprobar_impacto(self,x,y):
        print(f"[LOG] Comprobando impacto ({x},{y})") #Printea la casilla que has marcado.
        return self.casillero[x][y].disparar()




