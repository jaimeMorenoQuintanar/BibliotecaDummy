from Libro import Libro
from typing import List

# Definición de atributos
lista_libros: List[Libro] = []
id:int = 0
archivo_datos = open("biblioteca.txt", "r+")
counter:int= 0
SI = ["S", "s", "SÍ", "SI", "Sí", "sí", "si"]
NO = ["N", "n", "NO", "No", "no"]
# Definición de métodos
def imprimir_texto_ppal():
    print("BIBLIOTECA MUNICIPAL ENDER")
    print("#################################")
    print("1. Incluir libro")
    print("2. Borrar libro")
    print("3. Consultar libro")
    print("4. Consultar todos los libros disponibles")
    print("#################################")
    print("Seleccione una opción...")
    opcion_seleccionada = input()
    print("---------------------------------")
    return opcion_seleccionada

def implementar_modo_insercion(lista_libros):
    try:
        print("MODO INSERCIÓN")
        print(" ")
        print("Inserta título...")
        titulo = input()
        print("Inserta autor...")
        autor = input()
        print("Inserta editorial...")
        editorial = input()
        print("Inserta año...")
        anio = int(input())
        global id 
        id += 1
        libro_creado = Libro(id, titulo, autor, editorial, anio)
        lista_libros.append(libro_creado)

        print(f"Libro insertado con éxito con id: {libro_creado.id}")
    except:
        print("Error al insertar el nuevo libro")


def implementar_modo_borrado():
    try:
        print("MODO BORRADO")
        print(" ")
        print("Inserta id...")
        id = int(input())
        for libro in lista_libros:
            if libro.id == id:
                lista_libros.remove(libro)
                print(f"Libro con id: {libro.id} borrado con éxito")
                pass
        print("Libro no disponible en la biblioteca")
    except:
        print("Error al borrar el libro")
def implementar_modo_consulta_individual(lista_libros):
    print("MODO CONSULTA LIBRO")
    print(" ")
    print("Inserta id...")
    id = int(input())
    for libro in lista_libros:
        if libro.id == id:
            print("--------------------------")
            print(f"ID: {libro.id}")
            print(f"TÍTULO: {libro.titulo}")
            print(f"AUTOR: {libro.autor}")
            print(f"EDITORIAL: {libro.editorial}")
            print(f"AÑO: {libro.anio}")
            print("--------------------------")

def implementar_modo_consulta_biblioteca(lista_libros):
    print("MODO CONSULTA BIBLIOTECA")
    print(" ")

    for libro in lista_libros:
            print("--------------------------")
            print(f"ID: {libro.id}")
            print(f"TÍTULO: {libro.titulo}")
            print(f"AUTOR: {libro.autor}")
            print(f"EDITORIAL: {libro.editorial}")
            print(f"AÑO: {libro.anio}")
            print("--------------------------")

def presentar_opciones(lista_libros):
    opcion_seleccionada = imprimir_texto_ppal()
    if int(opcion_seleccionada) == 1:
        implementar_modo_insercion(lista_libros)
    elif int(opcion_seleccionada) == 2:
        implementar_modo_borrado()
    elif int(opcion_seleccionada) == 3:
        implementar_modo_consulta_individual(lista_libros)
    elif int(opcion_seleccionada) == 4:
        implementar_modo_consulta_biblioteca(lista_libros)
    else:
        print("La opción seleccionada no es válida")
    
    global counter
    counter += 1

def continuar():
    print("")
    print("¿Quiere continuar en la biblioteca? (S/N)")
    respuesta = input()
    if SI.__contains__(respuesta):
        presentar_opciones(lista_libros)
    elif NO.__contains__(respuesta):
        global counter
        counter = 0
        pass
    else:
        print("Responda S o N")
        continuar()

def escribir_archivo():
    global archivo_datos
    global lista_libros
    
    for libro in lista_libros:
        archivo_datos.write(f"{libro.id}#{libro.titulo}#{libro.autor}#{libro.editorial}#{libro.anio} \r\n")

def importar_datos():
    global lista_libros
    global archivo_datos
    lineas = archivo_datos.read().splitlines()
    for linea in lineas:
        if not linea:
            pass
        else:
            atributos_libro_archivo = linea.split("#")
            libro_archivo = devolver_libro_archivo(atributos_libro_archivo)
            lista_libros.append(libro_archivo)

def devolver_libro_archivo(atributos_libro_archivo):
    id = int(atributos_libro_archivo[0])
    titulo = atributos_libro_archivo[1]
    autor = atributos_libro_archivo[2]
    editorial = atributos_libro_archivo[3]
    anio = int(atributos_libro_archivo[4])
    libro_archivo = Libro(id, titulo, autor, editorial, anio)
    return libro_archivo
# Programa ppal

importar_datos()

presentar_opciones(lista_libros)

while counter != 0:
    continuar()

escribir_archivo()
archivo_datos.close()




