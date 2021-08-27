# from os import pipe
# import xml.etree.ElementTree as ET
# from xml.dom import minidom
# from ListaTerrenos import ListaTerrenos
# from Matriz import Matriz

# listaTerrenos = ListaTerrenos()
# terrenoSeleccionado = ""


# #Función para cargar el archivo xml - generar el terreno - crear las listas ortogonales de cada posición en el terreno
# def cargarArchivo(ruta):

#     tree = ET.parse(ruta)
#     root = tree.getroot()

#     #generando el terreno
#     for elemento in root:
#         nombreTerreno = elemento.attrib['nombre']
#         # print('Terreno: ',nombreTerreno)
#         for coordenandasInicio in elemento.iter('posicioninicio'):
#            pass
#         for coordenandasFin in elemento.iter('posicionfin'):
#            pass

#         listaTerrenos.agregarTerreno(nombreTerreno, coordenandasInicio[0].text, coordenandasInicio[1].text, coordenandasFin[0].text, coordenandasFin[1].text)
        
#         #generando lista ortogonal de las posiciones del terreno instanciado anteriormente
#         contador = 0
        
#         # print("Lista de posiciones en el terreno")
#         for subelemento in elemento.iter('posicion'):
#             # print("Posicion Y: ", subelemento.attrib['y'], "Posicion X: ", subelemento.attrib['x'], "Costo: ", subelemento.text)
#             terreno = listaTerrenos.getTerreno(nombreTerreno) #buscando el terreno al cual le vamos agregar su matriz de posiciones
#             terreno.matriz_Posiciones.insertar(subelemento.attrib['y'], subelemento.attrib['x'], subelemento.text)
#             contador+=1
#         # print(f"contador es igual a: {contador}")

# #Función para escribir el archivo de salida xml, también se especifica el nombre y ruta del archivo.
# def escribirArchivo(rutaSalida, terrenoSeleccionado):

#     root = ET.Element( f"{terrenoSeleccionado}")
#     posicioninicio = ET.SubElement(root, "posicioninicio")
#     ET.SubElement(posicioninicio, "x").text = f"{str(listaTerrenos.getTerreno(terrenoSeleccionado).x1)}"
#     ET.SubElement(posicioninicio, "y").text = f"{str(listaTerrenos.getTerreno(terrenoSeleccionado).y1)}"
#     posicionfin = ET.SubElement(root, "posicionfin")
#     ET.SubElement(posicionfin, "x").text = f"{str(listaTerrenos.getTerreno(terrenoSeleccionado).x2)}"
#     ET.SubElement(posicionfin, "y").text = f"{str(listaTerrenos.getTerreno(terrenoSeleccionado).y2)}"
#     combustible = ET.SubElement(root, "combustible")
#     combustible.text = f"{str(listaTerrenos.getTerreno(terrenoSeleccionado).getPosiciones().CombustibleCaminoMinimo)}"

#     for elementos in listaTerrenos.getTerreno(terrenoSeleccionado).getPosiciones().listaCaminoMinimo:
#         posicion = ET.SubElement(root, "posicion", x = f"{elementos[1]}", y = f"{elementos[0]}")
#         posicion.text = listaTerrenos.getTerreno(terrenoSeleccionado).getPosiciones().getPesoNodo(int(elementos[0]),int(elementos[1]))

#     arbol = ET.ElementTree(root)
#     arbol.write(rutaSalida)

# #======================================================FUNCIÓN MAIN==================================================
# if __name__ == "__main__":
#     while(True):
#         print('''Bienvenido Usuario
#         ===================MENÚ=================
#         1. Cargar archivo
#         2. Procesar archivo
#         3. Escribir archivo de salida
#         4. Mostrar datos del estudiante
#         5. Generar gráfica
#         6. Salida
#         ===================MENÚ=================''')
#         #Escogiendo una opción del menú
#         try:
#             opcion = int(input("Escoga una opción para continuar: "))
#             if opcion == 1:
#                 try:
#                     listaTerrenos = ListaTerrenos()
#                     print("Escogió la opción 1 - Cargar archivo ")
#                     rutaArchivo = input('Ingrese la ruta del archivo:')
#                     cargarArchivo(rutaArchivo)
#                     print("\nArchivo cargado con éxito!!!")
#                     # print(listaTerrenos.getTerreno("terreno1").getPosiciones().mostrarMatrizFilas())
#                 except:
#                     print("\nIngrese la ruta de un archivo válido.")
                
#                 # listaTerrenos.getTerreno("terreno1").getPosiciones().caminoMinimoMatriz(1,1,5,5)
#                 # print(listaTerrenos.getTerreno("terreno1").getPosiciones().mostrarMatrizMejorCamino())
#                 # listaTerrenos.getTerreno("terreno2").getPosiciones().imprimirMatriz("terreno2")
#                 input("Presione ENTER para continuar...")
#             elif opcion == 2:
#                 print("Escogió la opción 2 - Procesar archivo\n")
#                 if(listaTerrenos.longitud == 0):
#                     print("Actualmente no hay terrenos cargados al sistema.")
#                 else:
#                     try:
#                         listaTerrenos.mostrarTerrenos()
#                         terrenoSeleccionado = input('Ingrese el nombre del terreno a procesar: ')
#                         #Guardar las coordenadas de inicio y fin del terreno seleccionando.
#                         x1 = int(listaTerrenos.getTerreno(terrenoSeleccionado).x1)
#                         y1 = int(listaTerrenos.getTerreno(terrenoSeleccionado).y1)
#                         x2 = int(listaTerrenos.getTerreno(terrenoSeleccionado).x2)
#                         y2 = int(listaTerrenos.getTerreno(terrenoSeleccionado).y2)
#                         #Llamando a funciones para el camino Minimo y mapeo del mismo
#                         listaTerrenos.getTerreno(terrenoSeleccionado).getPosiciones().caminoMinimoMatriz(y1,x1,y2,x2)
#                         combustibleMejorCamino = listaTerrenos.getTerreno(terrenoSeleccionado).getPosiciones().CombustibleCaminoMinimo
#                         print(f"\nTerreno seleccionado: {terrenoSeleccionado}")
#                         listaTerrenos.getTerreno(terrenoSeleccionado).getPosiciones().mostrarMatrizMejorCamino()
#                         print(f"El combustible total que la ruta consumirá es de: {combustibleMejorCamino} Unidades\n")
#                     except:
#                         print("\nNombre de terreno inválido, intenté de nuevo.")
                    
#                 input("Presione ENTER para continuar...")
#             elif opcion == 3:
#                 print("Escogió la opción 3 - Escribir archivo de salida\n")
#                 # rutaArchivo = input("Ingrese el nombre del archivo: ")
#                 # file = './' + Filename
#                 if(terrenoSeleccionado == ""):
#                     print("No se ha procesado ningún terreno aún.")
#                 else:
#                     try:
#                         rutaArchivo = input("Ingrese la ruta del archivo de salida: ")
#                         escribirArchivo(rutaArchivo, terrenoSeleccionado)
#                         print(f"Se escribió el archivo de salida del terreno procesado: {terrenoSeleccionado}")
#                         print("Archivo de salida escrito con éxito.\n")
#                     except:
#                         print("Ingrese una ruta de salida válida.\n")

#                 input("Presione ENTER para continuar...")
#             elif opcion == 4:
#                 print("Escogió la opción 4 - Mostrar datos del estudiante")
#                 print('''           
#                             Diego André Mazariegos Barrientos
#                                        202003975
#                 Introducción a la programación y computación 2 sección "D"
#                             Ingenieria en Ciencias y Sistemas
#                                       4to Semestre\n''')
#                 input("Presione ENTER para continuar...")
#             elif opcion == 5:
#                 print("Escogió la opción 5 - Generar gráfica\n")
#                 if(listaTerrenos.longitud == 0):
#                     print("Actualmente no hay terrenos cargados al sistema.")
#                 else:
#                     try:
#                         listaTerrenos.mostrarTerrenos()
#                         terrenoSeleccionado = input('Ingrese el nombre del terreno a procesar: ') 
#                         listaTerrenos.getTerreno(terrenoSeleccionado).getPosiciones().imprimirMatriz(terrenoSeleccionado)
#                         print("Terreno impreso con éxito.\n")
#                     except:
#                         print("\nIngrese un nombre de terreno válido.")
#                 input("Presione ENTER para continuar...")
#             elif opcion == 6:
#                 print("Escogió la opción 6 - Salir")
#                 input("Presione ENTER para continuar...")
#                 break
#             else:
#                 print("\nEscoga una opción válida del menú")
#                 input("Presione ENTER para continuar...")
#         except:
#             print("\nÚnicamente se aceptan números enteros")
#             input("Presione ENTER para continuar...")
            
