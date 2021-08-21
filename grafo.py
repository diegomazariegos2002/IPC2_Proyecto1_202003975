import xml.etree.cElementTree as ET

rutaSalida = "prueba2.xml"

root = ET.Element("terreno")
posicioninicio = ET.SubElement(root, "posicioninicio")
ET.SubElement(posicioninicio, "x").text = "1"
ET.SubElement(posicioninicio, "y").text = "2"
posicionfin = ET.SubElement(root, "posicionfin")
ET.SubElement(posicionfin, "x").text = "3"
ET.SubElement(posicionfin, "y").text = "4"
combustible = ET.SubElement(root, "combustible")
combustible.text = "9999"
posicion = ET.SubElement(root, "posicion", x = "5", y = "6")
posicion.text = "valores xy"

arbol = ET.ElementTree(root)
arbol.write(rutaSalida)



