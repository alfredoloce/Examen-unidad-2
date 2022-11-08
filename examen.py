import json

municipios = {}
bd = []
datos = []
diccionario = dict()

def obtenerdatos():
    fh= open("CPdescarga.txt")
    contador = 0
    for linea in fh:
        palabras = linea.rstrip().split('|')
        print(palabras)
        for palabra in palabras:
            if not palabra in diccionario:
                diccionario[palabra] = contador
                contador += 1
    ##print(diccionario)

def ingresardatos():
    try:
        D_mnpio = input("Ingrese el nombre del Municipio")
        d_codifo = input("Ingrese el codigo postal")
        d_tipo_asenta = input("Ingrese tipo de asentamiento")
        d_estado = input("Estado donde se encuentra")
        d_zona = input("Tipod de zona 'Urbano' o 'Rural'")
    except EOFError:
        print("Dato vacio volver a ingresar")


    municipios['d_codifo'] = d_codifo
    municipios['D_mnpio'] = D_mnpio
    municipios['d_tipo_asenta'] = d_tipo_asenta
    municipios['d_estado'] = d_estado
    municipios['d_zona'] = d_zona
    
    bd.append(municipios)

    for i in bd:
        print(i)

    with open('datos.json', 'w') as archivo:
        json.dump(bd, archivo)
        print("Archivo exportado")


def leerarchivo():
    with open('datos.json', 'r') as archivo:
        bd = json.load(archivo)
        print(bd)
        print("Obtenido exitosamente")

##ingresardatos()
##leerarchivo()

obtenerdatos()