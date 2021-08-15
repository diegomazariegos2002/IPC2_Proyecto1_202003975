import xml.etree.ElementTree as ET
from xml.dom import minidom
from ListaTerrenos import ListaTerrenos
from Matriz import Matriz

listaTerrenos = ListaTerrenos()


#Función para cargar el archivo xml - generar el terreno - crear las listas ortogonales de cada posición en el terreno
def cargarArchivo(ruta):

    tree = ET.parse(ruta)
    root = tree.getroot()

    #generando el terreno
    for elemento in root:
        nombreTerreno = elemento.attrib['nombre']
        # print('Terreno: ',nombreTerreno)
        for coordenandasInicio in elemento.iter('posicioninicio'):
           pass
        for coordenandasFin in elemento.iter('posicionfin'):
           pass

        listaTerrenos.agregarTerreno(nombreTerreno, coordenandasInicio[0].text, coordenandasInicio[1].text, coordenandasFin[0].text, coordenandasFin[1].text)
        
        #generando lista ortogonal de las posiciones del terreno instanciado anteriormente
        contador = 0
        
        # print("Lista de posiciones en el terreno")
        for subelemento in elemento.iter('posicion'):
            # print("Posicion Y: ", subelemento.attrib['y'], "Posicion X: ", subelemento.attrib['x'], "Costo: ", subelemento.text)
            terreno = listaTerrenos.getTerreno(nombreTerreno) #buscando el terreno al cual le vamos agregar su matriz de posiciones
            terreno.matriz_Posiciones.insertar(subelemento.attrib['y'], subelemento.attrib['x'], subelemento.text)
            contador+=1
        # print(f"contador es igual a: {contador}")


#======================================================FUNCIÓN MAIN==================================================
if __name__ == "__main__":
    while(True):
        print('''Bienvenido Usuario
        ===================MENÚ=================
        1. Cargar archivo
        2. Procesar archivo
        3. Escribir archivo salida
        4. Mostrar datos del estudiante
        5. Generar gráfica
        6. Salida
===================MENÚ=================''')
        #Escogiendo una opción del menú
        opcion = int(input("Escoga una opción para continuar: "))
        if opcion == 1:
            print("Escogió la opción 1")
                # Filename = input('Ingrese nombre de archivo:')
            # file = './' + Filename
            file = "./prueba.xml"
            cargarArchivo(file)
            # listaTerrenos.mostrarTerrenos()
            print(listaTerrenos.getTerreno("terreno2").getPosiciones().mostrarMatrizFilas())
            # print(listaTerrenos.getTerreno("terreno1").getPosiciones().mostrarMatrizColumnas())
            # print(listaTerrenos.getTerreno("terreno1").getPosiciones().getPesoNodo(4,3))
            # print(listaTerrenos.getTerreno("terreno1").getPosiciones().getNodo(4,3))
            # print(listaTerrenos.getTerreno("terreno1").getPosiciones().getNodo(1,2))
            # listaTerrenos.getTerreno("terreno1").getPosiciones().recorrerProfundidadPrimeroMatriz(1,4)
            listaTerrenos.getTerreno("terreno2").getPosiciones().caminoMinimoMatriz(1,1,4,6)
            print(listaTerrenos.getTerreno("terreno2").getPosiciones().mostrarMatrizMejorCamino())
            input("Presione ENTER para continuar...")
        elif opcion == 2:
            print("Escogió la opción 2")
        elif opcion == 3:
            print("Escogió la opción 3")
        elif opcion == 4:
            print("Escogió la opción 4")
        elif opcion == 5:
            print("Escogió la opción 5")
        elif opcion == 6:
            print("Escogió la opción 6")
            break
        else:
            print("Escoga una opción válida")

