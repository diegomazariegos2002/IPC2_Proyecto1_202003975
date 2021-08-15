from Matriz import Matriz

class Terrenos:
    def __init__(self, nombre = None, x1 = None, y1 = None, x2 = None, y2 = None, sig = None):
        self.nombre = nombre
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.matriz_Posiciones = Matriz()
        self.sig = sig

    def __str__(self):
        return f'''nombre del terreno: {self.nombre}
        X inicial: {self.x1}
        Y inicial: {self.y1}
        X final: {self.x2}
        Y final: {self.y2}'''

    def getPosiciones(self):
        return self.matriz_Posiciones
    

