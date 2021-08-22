from NodoPosicion import NodoEncabezado, NodoPosicion
from EncabezadoMatriz import listaEncabezado
#Librería utilizada para graficar grafos
from graphviz import Graph

class Matriz:
    def __init__(self):
        self.eFilas = listaEncabezado()
        self.eColumnas = listaEncabezado()
        self.listaCaminoMinimo = []
        self.CombustibleCaminoMinimo = None
    
    def insertar(self, fila, columna, valor):
        nuevo = NodoPosicion(fila, columna, valor)

        #Inserción encabezado por filas. (esto es extraído del video/conferencia) me sirvió mucho :D
        eFila = self.eFilas.getEncabezado(fila)
        if eFila == None:
            eFila = NodoEncabezado(fila)
            eFila.accesoNodo = nuevo
            self.eFilas.setEncabezado(eFila)
        else:
            if nuevo.columna < eFila.accesoNodo.columna:
                nuevo.derecha = eFila.accesoNodo
                eFila.accesoNodo.izquierda = nuevo
                eFila.accesoNodo = nuevo
            else:
                actual = eFila.accesoNodo
                while actual.derecha != None:
                    if nuevo.columna < actual.derecha.columna:
                        nuevo.derecha = actual.derecha
                        actual.derecha.izquierda = nuevo
                        nuevo.izquierda = actual
                        actual.derecha = nuevo
                        break
                    actual = actual.derecha
                
                if actual.derecha == None:
                    actual.derecha = nuevo
                    nuevo.izquierda = actual

        #Inserción encabezado por columnas. (esto es extraído del video/conferencia) me sirvió mucho :D
        eColumna = self.eColumnas.getEncabezado(columna)
        if eColumna == None:
            eColumna = NodoEncabezado(columna)
            eColumna.accesoNodo = nuevo
            self.eColumnas.setEncabezado(eColumna)
        else:
            if nuevo.fila < eColumna.accesoNodo.fila:
                nuevo.abajo = eColumna.accesoNodo
                eColumna.accesoNodo.arriba = nuevo
                eColumna.accesoNodo = nuevo
            else:
                actual = eColumna.accesoNodo
                while actual.abajo != None:
                    if nuevo.fila < actual.abajo.fila:
                        nuevo.abajo = actual.abajo
                        actual.abajo.arriba = nuevo
                        nuevo.arriba = actual
                        actual.abajo = nuevo
                        break
                    actual = actual.abajo
                
                if actual.abajo == None:
                    actual.abajo = nuevo
                    nuevo.arriba = actual

    def mostrarMatrizFilas(self):
        matrizGrafica = ''''''
        eFila = self.eFilas.primero
        print("=============================Matriz por FILAS=============================\n")
        while eFila != None:
            actual = eFila.accesoNodo
            while actual != None:
                matrizGrafica = matrizGrafica + f'''[{str(actual.fila)}][{str(actual.columna)}]({str(actual.valor)})'''  
                matrizGrafica = matrizGrafica + "   "
                actual = actual.derecha
            matrizGrafica = matrizGrafica + "\n"
            eFila = eFila.siguiente
        print(matrizGrafica)

    def mostrarMatrizColumnas(self):
        matrizGrafica = ''''''
        eColumna = self.eColumnas.primero
        print("=============================Matriz por COLUMNAS=============================\n")
        while eColumna != None:
            actual = eColumna.accesoNodo
            while actual != None:
                matrizGrafica = matrizGrafica + f'''[{str(actual.fila)}][{str(actual.columna)}]({str(actual.valor)})'''  
                matrizGrafica = matrizGrafica + "\n"
                actual = actual.abajo
            matrizGrafica = matrizGrafica + "   "
            eColumna = eColumna.siguiente
        print(matrizGrafica)
    
    def getPesoNodo(self, fila, columna):
        eFila = self.eFilas.primero
        while eFila != None:
            actual = eFila.accesoNodo
            while actual != None:
                if(int(actual.fila) == fila and int(actual.columna) == columna):
                    return actual.valor
                actual = actual.derecha
            eFila = eFila.siguiente
        return "No existe el nodo para ver su peso"
    
    def getNodo(self, fila, columna):
        eFila = self.eFilas.primero
        while eFila != None:
            actual = eFila.accesoNodo
            while actual != None:
                if(int(actual.fila) == fila and int(actual.columna) == columna):
                    return actual
                actual = actual.derecha
            eFila = eFila.siguiente
        return "ese nodo no existe"

    #Función encargada de imprimir por medio de la librería graphviz la matriz ortogonal en pdf.
    def imprimirMatriz(self, nombreTerreno):
        dot = Graph(comment='The Round Table')

        dot.attr('node', shape = "plaintext")

        dot.node('titulo',label=f'{nombreTerreno}',)

        dot.attr('node', shape = "rectangle")
        
        eFila = self.eFilas.primero
        print("=============================Matriz por FILAS=============================\n")
        while eFila != None:
            actual = eFila.accesoNodo
            while actual != None:
                #Creando los nodos donde antes de la "," hace referencia al id del nodo y después de la "," al valor del label osea
                #el valor que aparece impreso en el nodo.
                dot.node(f'{str(actual.fila)}{str(actual.columna)}',f'({str(actual.fila)},{str(actual.columna)}){str(actual.valor)}')
                #Esta parte de if's son los responsables de crear la uniones entre los nodos a sus vez el constraint es que se utiliza
                #para poner todos los nodos en sus respectivas posiciones.
                if(actual.derecha != None):
                    dot.edge(f'{str(actual.fila)}{str(actual.columna)}',f'{str(actual.derecha.fila)}{str(actual.derecha.columna)}',constraint = 'false')
                if(actual.abajo != None):
                    dot.edge(f'{str(actual.fila)}{str(actual.columna)}',f'{str(actual.abajo.fila)}{str(actual.abajo.columna)}',constraint = 'true')
                actual = actual.derecha
            eFila = eFila.siguiente

        # Guarde la fuente en el archivo y proporcione el motor Graphviz
        dot.render('Terreno', view=True)


    #Esta función muestra la matriz por medio de filas pero con 0 los caminos no tomados 
    #y con 1 los caminos que son los mejores para llegar al camino mínimo de mi matriz.       
    def mostrarMatrizMejorCamino(self):
        matrizGrafica = ''''''
        eFila = self.eFilas.primero
        print("=============================Matriz Con Camino Mínimo=============================\n")
        while eFila != None:
            actual = eFila.accesoNodo
            while actual != None:
                if self.buscarExistenciaEnLista(self.listaCaminoMinimo, [actual.fila, actual.columna]) == True:
                        matrizGrafica = matrizGrafica + f'''| 1 |'''
                else:
                        matrizGrafica= matrizGrafica + f'''| 0 |'''
                actual = actual.derecha
            matrizGrafica = matrizGrafica + "\n"
            eFila = eFila.siguiente
        print(matrizGrafica)

    #Función que se encarga de ver si las coordenadas de un nodo estan en las coordenadas de la lista 
    #de caminos mínimos
    def buscarExistenciaEnLista(self, lista1, lista2):
        for sublistas in lista1:
            if sublistas == lista2:
                return True
        return False

    #Función para recorrer todo mi matriz de nodos desde un nodo cualquiera elegido
    def recorrerProfundidadPrimeroMatriz(self, origenFila, origenColumna, elementosRecorridos = []):
        #aquí se aguarda el objeto NodoPosicion como tal el cual su espacio en memoria funciona como id
        nodoActual = self.getNodo(origenFila, origenColumna)
        #si nodoActual existe en la lista de elementos recorridos
        if nodoActual in elementosRecorridos:
            return
        print("Nodo en la fila: ", nodoActual.fila, "Nodo en la columna: ", nodoActual.columna)
        elementosRecorridos.append(nodoActual)
        #Vecinos del grafo/nodo en la matriz ----- Parte recursiva del programa
        if nodoActual.derecha != None:
            self.recorrerProfundidadPrimeroMatriz(int(nodoActual.derecha.fila), int(nodoActual.derecha.columna), elementosRecorridos)
        if nodoActual.izquierda != None:
            self.recorrerProfundidadPrimeroMatriz(int(nodoActual.izquierda.fila), int(nodoActual.izquierda.columna), elementosRecorridos)
        if nodoActual.arriba != None:
            self.recorrerProfundidadPrimeroMatriz(int(nodoActual.arriba.fila), int(nodoActual.arriba.columna), elementosRecorridos)
        if nodoActual.abajo != None:
            self.recorrerProfundidadPrimeroMatriz(int(nodoActual.abajo.fila), int(nodoActual.abajo.columna), elementosRecorridos)

    #Función para determinar el camino minimo en la matriz.
    def caminoMinimoMatriz(self, origenFila, origenColumna, destinoFila, destinoColumna):
        nodoOrigen = self.getNodo(origenFila, origenColumna)
        nodoDestino = self.getNodo(destinoFila, destinoColumna)
        etiquetas = {nodoOrigen:(0,None)}
        self.dijkstra(nodoDestino, etiquetas, [])
        #la función .get aquí es una función de los diccionarios en python. (no confundir y pensar que fue creada aquí)
        self.CombustibleCaminoMinimo = etiquetas.get(nodoDestino)[0]
        # print("Combustible utilizado", self.CombustibleCaminoMinimo)
        self.listaCaminoMinimo = self.construirCaminodeRegreso(etiquetas, nodoOrigen, nodoDestino)
    
    #Función para construir el camino de regreso una vez ya llegado al nodo de destino ---- esta función se ejecuta cuando
    #termina la recursividad de la función dijkstra y recorre todo el camino del destino al comienzo osea 
    # de final al comienzo realizando su recorrido mediante las etiquetas.
    def construirCaminodeRegreso(self, etiquetas, origen, destino):
        # print("[",origen.fila,"]","[",origen.columna,"]","->","[",destino.fila,"]","[",destino.columna,"]")
        if origen == destino:
            return [[origen.fila, origen.columna]]
        return self.construirCaminodeRegreso(etiquetas, origen, self.anterior(etiquetas[destino])) + [[destino.fila, destino.columna]]

    #Una etiqueta es basicamente de la forma etiqueta(nodo)=(peso_Acumulado, nodo_Anterior) 
    def anterior(self, etiqueta):
        return etiqueta[1]

    #Básicamente esta función es la encargada de realizar todo lo que viene siendo lo de ir eligiendo el camino mas corto
    #e ir poniendo las etiquetas y así. (podría decirse que es la principal del algoritmo)
    #realmente esta parte de aquí se entiende mejor con el debugger y ya conociendo la teoría.
    def dijkstra(self, destino, etiquetas, procesados):
        nodoActual = self.menorValorNoProcesado(etiquetas,procesados)
        if nodoActual == destino:
            return
        procesados.append(nodoActual)
        for vecino in self.vecinoNoProcesado(nodoActual, procesados):
            self.generarEtiqueta(vecino, nodoActual, etiquetas)
        self.dijkstra(destino, etiquetas, procesados)
    
    #Función de generar la etiqueta como tal y guarda el nodo anterior y el acumulado
    #basicamento esta función lo que realiza es que si se conoce la teoría 
    #me registra mis etiquetas a lo largo del camino. (Esta parte con la teoría se identifica mejor)
    def generarEtiqueta(self, nodo, anterior, etiquetas):
        etiquetaNodoAnterior = etiquetas[anterior]
        etiquetaPropuesta = int(self.getPesoNodo(int(nodo.fila), int(nodo.columna))) + int(self.acumulado(etiquetaNodoAnterior)), anterior  
        if (nodo not in etiquetas) or (int(self.acumulado(etiquetaPropuesta)) < self.acumulado(etiquetas[nodo])):                          
            etiquetas.update({nodo:etiquetaPropuesta})                                                                                     
                                                                                                                                            
    def acumulado(self, etiqueta):
        return etiqueta[0]

    #Mediante esta función obtenemos todas las conexiones que tiene el nodo con las coordenadas respectivas
    # y aguardamos estas relaciones en una lista.
    def aristas(self, coordenadaFilaNodo, coordenadaColumnaNodo):

        nodoActual = self.getNodo(coordenadaFilaNodo, coordenadaColumnaNodo)
        relaciones = []
        if nodoActual.derecha != None:
            relaciones.append(nodoActual.derecha)
        if nodoActual.izquierda != None:
            relaciones.append(nodoActual.izquierda)
        if nodoActual.arriba != None:
            relaciones.append(nodoActual.arriba)
        if nodoActual.abajo != None:
            relaciones.append(nodoActual.abajo)
        return relaciones
    
    #En esta función basicamente lo que realizo es ver todas las relaciones que tiene un nodo
    #a esas relaciones les decimos vecinos pues son vecinos de ese nodo y con el filtro lo que hacemos
    #es verificar si esos vecinos no han sido verificados ya, puesto que según el algoritmo 
    #si ya han sido procesados quiere decir que ya hemos pasado por ellos y no hay necesidad de volver 
    #a verlos, es como una forma de evitar ciclos infinitos yendo del nodo actual a su nodo anterior y así
    #infinitamente.
    def vecinoNoProcesado(self, nodo, procesados):
        aristasdeVecinosNoProcesados = list(filter(lambda x: not x in procesados, self.aristas(int(nodo.fila), int(nodo.columna))))
        return [arista for arista in aristasdeVecinosNoProcesados ]
    
    #Esta función va a ser básicamente la que me ayude a movilizarme de nodo en nodo
    #puesto que mi etiquetadosSinProcesar aguardara a todos aquellos que se tengan 
    #pero que no esten ya procesados y cuando decimos que un nodo esta procesado
    #nos referimos ya sea al nodo principal o todo aquel nodo al cual ya se paso por el
    # como la función vecinoNoProcesado pero con la excepción de que aquí escogemos
    # El vecino con menor valor de todos.
    def menorValorNoProcesado(self, etiquetas, procesados):
        etiquetadosSinProcesar = {k:[v,y] for (k,[v,y]) in etiquetas.items() if k not in procesados}.items()
        return min(etiquetadosSinProcesar, key=lambda acum: acum[1][0])[0] 

        #Resumen: el error aquí sucede porque yo hago un min de objetos.

        #Creo que el error se genera ya que min mide valores y en realidad cuando pongo acum estoy midiendo el objeto 
        #debería ser tal vez key = lambda acum: acum[0] recordando que el concepto de tupla 
        #donde si yo declaro el key este se utilizar para decirle al metodo de ordenamiento 
        #a partir de que casilla en la tupla yo quiero ordenar mis elementos obviamente el return min()[0]
        #si es válido porque lo que yo quiero retornar es el primer valor de la lista con el min()
        #ya que una lista con min() va del valor mas pequeño al mas grande. 
        #IMPORTANTE: esto era un error que tuve mediante la realizción pero dejo la nota porque 
        #me pareció muy curioso y no quiero olvidarme de el.

        

