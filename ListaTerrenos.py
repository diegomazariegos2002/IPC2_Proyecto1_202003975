from Terrenos import Terrenos

class ListaTerrenos:
    def __init__(self):
        self.primero = None
        self.longitud = 0
    
    def agregarTerreno(self, nombre, x1, y1, x2, y2):
        nuevoTerreno = Terrenos(nombre, x1, y1, x2, y2)
        if self.primero == None:
            self.primero = nuevoTerreno
            return
        #Nos posiciona en el último nuevoTerreno de la lista.
        aux = self.primero
        while aux.sig != None:
            aux = aux.sig
        #Aquí se agrega el nuevo nuevoTerreno al final de la lista osea en la cola.
        aux.sig = nuevoTerreno
        self.longitud += 1

    def mostrarTerrenos(self):
        aux = self.primero
        while aux != None:
            print(aux)
            aux = aux.sig
    
    def getTerreno(self, nombre):
        tmp = self.primero
        while tmp is not None:
            if tmp.nombre == nombre:
                return tmp
            tmp = tmp.sig
        return None
        