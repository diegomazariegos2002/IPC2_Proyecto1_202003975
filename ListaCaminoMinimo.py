#CAMBIO
class NodoCaminoMinimo:
    def __init__(self, fila, columna, sig = None):
        self.fila = fila
        self.columna = columna
        self.sig = sig

class ListaCaminoMinimo:
    def __init__(self) -> None:
        self.primero = None
        self.longitud = 0

    def agregarNodoCaminoMinimo(self, fila, columna):
        nodoCaminoMinimo = NodoCaminoMinimo(fila, columna)
        if self.primero == None:
            self.primero = nodoCaminoMinimo
            return
        #Nos posiciona en el último nuevoTerreno de la lista.
        aux = self.primero
        while aux.sig != None:
            aux = aux.sig
        #Aquí se agrega el nuevo nuevoTerreno al final de la lista osea en la cola.
        aux.sig = nodoCaminoMinimo
        self.longitud += 1

    def mostrarCamino(self):
        aux = self.primero
        while aux != None:
            print(f"[{aux.fila},{aux.columna}]")
            aux = aux.sig

    def buscarExistencia(self, fila, columna):
        aux = self.primero
        while aux != None:
            if aux.fila == fila and aux.columna == columna:
                return True
            aux = aux.sig
        return False