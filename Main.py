import xml.etree.ElementTree as ET
from xml.dom import minidom
from ListaTerrenos import ListaTerrenos
from Matriz import Matriz

listaTerrenos = ListaTerrenos()
terrenoSeleccionado = ""


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

#Función para escribir el archivo de salida xml, también se especifica el nombre y ruta del archivo.
def escribirArchivo(rutaSalida):
    global terrenoSeleccionado

    root = ET.Element( f"{terrenoSeleccionado}")
    posicioninicio = ET.SubElement(root, "posicioninicio")
    ET.SubElement(posicioninicio, "x").text = f"{str(listaTerrenos.getTerreno(terrenoSeleccionado).x1)}"
    ET.SubElement(posicioninicio, "y").text = f"{str(listaTerrenos.getTerreno(terrenoSeleccionado).y2)}"
    posicionfin = ET.SubElement(root, "posicionfin")
    ET.SubElement(posicionfin, "x").text = f"{str(listaTerrenos.getTerreno(terrenoSeleccionado).x2)}"
    ET.SubElement(posicionfin, "y").text = f"{str(listaTerrenos.getTerreno(terrenoSeleccionado).y2)}"
    combustible = ET.SubElement(root, "combustible")
    combustible.text = f"{str(listaTerrenos.getTerreno(terrenoSeleccionado).getPosiciones().CombustibleCaminoMinimo)}"

    for elementos in listaTerrenos.getTerreno(terrenoSeleccionado).getPosiciones().listaCaminoMinimo:
        posicion = ET.SubElement(root, "posicion", x = f"{elementos[1]}", y = f"{elementos[0]}")
        posicion.text = listaTerrenos.getTerreno("terreno1").getPosiciones().getPesoNodo(int(elementos[0]),int(elementos[1]))

    arbol = ET.ElementTree(root)
    arbol.write(rutaSalida)

#======================================================FUNCIÓN MAIN==================================================
if __name__ == "__main__":
    while(True):
        print('''Bienvenido Usuario
        ===================MENÚ=================
        1. Cargar archivo
        2. Procesar archivo
        3. Escribir archivo de salida
        4. Mostrar datos del estudiante
        5. Generar gráfica
        6. Salida
===================MENÚ=================''')
        #Escogiendo una opción del menú
        opcion = int(input("Escoga una opción para continuar: "))
        if opcion == 1:
            print("Escogió la opción 1 - Cargar archivo ")
            terrenoSeleccionado = "terreno1"
            rutaArchivo = input('Ingrese la ruta del archivo:')
            cargarArchivo(rutaArchivo)
            print(listaTerrenos.getTerreno("terreno1").getPosiciones().mostrarMatrizFilas())
            # listaTerrenos.getTerreno("terreno1").getPosiciones().caminoMinimoMatriz(1,1,5,5)
            # print(listaTerrenos.getTerreno("terreno1").getPosiciones().mostrarMatrizMejorCamino())
            # listaTerrenos.getTerreno("terreno2").getPosiciones().imprimirMatriz("terreno2")
            input("Presione ENTER para continuar...")
        elif opcion == 2:
            print("Escogió la opción 2 - Procesar archivo")
        elif opcion == 3:
            print("Escogió la opción 3 - Escribir archivo de salida")
            # Filename = input("Ingrese el nombre del archivo: ")
            # file = './' + Filename
            file = "./prueba2.xml"
            escribirArchivo(file)
            input("Presione ENTER para continuar...")
        elif opcion == 4:
            print("Escogió la opción 4 - Mostrar datos del estudiante")
        elif opcion == 5:
            print("Escogió la opción 5 - Generar gráfica")
        elif opcion == 6:
            print("Escogió la opción 6 - Salir")
            break
        else:
            print("Escoga una opción válida")

