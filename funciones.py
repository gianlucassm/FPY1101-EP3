"""Una biblioteca necesita desarrollar una aplicación que permita gestionar el préstamo de libros y calcular el total de
libros prestados por cada usuario. La aplicación debe cumplir con las siguientes funcionalidades:"""




import os
#1. Registrar libro
"""Registrar libro
Para registrar un libro se requiere los siguientes datos: Título, Autor, Año de Publicación, SKU. Debe validar que
todos los datos sean ingresados."""
libros = []
prest = []
def reg_libro():
    try:
        print("registre los siguientes datos de el libro: Título, Autor, Año de Publicación, SKU. ")
        print("Nota: El SKU es el identificador único de cada libro, facilitando su búsqueda y adquisición en librerías y bibliotecas.Ejemplo de SKU es las 6 primeras letras del título del libro – las 3 primeras letras del autor – año de publicación.")
        titulo = input("ingrese el titulo del libro")
        autor = input("ingrese el autor del libro")
        año = int(input("ingrese el año de publicacion del libro "))
        sku = input("ingrese el sku")
        #validador
        if titulo == "" or autor == "" or año <= 0 or sku == 0:
            print("debe ingresar todos los campos")
        else:
            libro = {
                'titulo': titulo,
                'autor': autor,
                'año': año,
                'sku': sku
            }
            libros.append(libro)

    except ValueError:
        print("debe llenar todos los campo")
#2. Prestar libro
"""""Prestar libro
Para prestar un libro se requiere: Nombre del usuario y SKU del libro. Debe validar que el libro exista y que no esté
ya prestado."""""
def prest_libro():
    try:
        print("titulo\t\tautor\t\taño\t\tsku")
        for libro in libros:
            print(f"{libro["titulo"]}\t\t{libro["autor"]}\t\t{libro["año"]}\t\t{libro["sku"]}\n\n")
        print("para prestar un libro necesitamos la siguiente informacion")
        print("usuario, sku ")
        usuario = input()
        sku = input()
        #validador
        if usuario == "" or sku == "":
            print("debe ingresar todos los campos")
        elif sku in prest:
            print("libro prestado")
        else:
            prestar = {
                'usuario': usuario,
                'sku': sku
            }
            prest.append(prestar)
    except ValueError:    
#3. Listar todos los libros
        "Listar todos los libros Debe mostrar en la pantalla la lista de todos los libros registrados."
def listar_libro():
    print("titulo\t\tautor\t\taño\t\tsku")
    for libro in libros:
           print(f"{libro["titulo"]}\t\t{libro["autor"]}\t\t{libro["año"]}\t\t{libro["sku"]}\n\n")
#4. Imprimir reporte de préstamos
def imprimir():
    with open ("planilla_libros","w") as archivo:
        archivo.write("usuario\t\tsku")
        for sku in prest:
            archivo.write(f"{prest["usuario"]}\t\t{prest["sku"]}")
        print("listado guardado en",os.getcwd())
#5. Salir del Programa
def exit():
    print("programado por: GIAN LUCAS SAN MARTIN\n rut: 199221351-2")
#menu
def menu():
    while True:
        try:
            print("bienvenido a tu librerira online\n")
            print("1. Registrar libro")
            print("2. Prestar libro")
            print("3. Listar todos los libros")
            print("4. Imprimir reporte de préstamos")
            print("5. Salir del Programa\n")
            op = int(input("ingresea una opcion"))
        except ValueError:
            print("ingrese una opcion valida, intente nuevamente")
        if op == 1:
                reg_libro()
        if op == 2:
                prest_libro()
        if op == 3:
                listar_libro()
        if op == 4:
                imprimir()
        if op == 5:
            exit()
            break
        else:
            print("opcion invalida")
       

"""Cada una de estas opciones de la aplicación debe estar desarrollada en una función que debe ser llamada desde el
programa principal."""









