import os
from os import system
from pathlib import Path, PureWindowsPath


def bienvenida():
    nombre = input('Escriba su nombre: \n')
    print(f'Bienvenido {nombre} al Recetario de Cocina Venezolana\n\n')
    return nombre


def mostrar_rutas():
    carpeta = Path(Path.home(), "Documents", "Curso python udemy", "Dia 6", "Recetas")
    print(f'Las recetas están en: {carpeta}')
    return carpeta


def contador_de_recetas():
    contador = 0

    for numero, txt in enumerate(Path('Recetas').glob('**/*.txt')):
        contador = numero
    print(f"Tienes un total de {contador + 1} recetas\n")


def panel_de_opciones():
    opcion = '0'
    while opcion != '6':

        print('-' * 70 + '\n')
        print(f' Has entrado al panel de opciones del Recetario de Cocina Venezolana\n')
        print('-' * 70)
        print('Escoja una opción: \n')
        ruta = mostrar_rutas()
        opcion = input(
            " Opción 1: Para leer recetas\n Opcion 2: Crear Receta\n Opción 3: Crear Categoria\n Opción 4: Eliminar Receta\n Opción 5: Eliminar Categoria\n Opción 6: Finalizar\n")
        print(opcion)
        match opcion:
            case '1':
                lista_total = mostrar_categorias(ruta)
                categoria_elegida = elegir_categoria(lista_total)
                receta_elegida = elegir_receta(categoria_elegida)
                mostrar_recetas(receta_elegida, categoria_elegida)
            case '2':
                lista_total = mostrar_categorias(ruta)
                categoria_elegida = elegir_categoria(lista_total)
                crear_recetas(categoria_elegida)

            case '3':
                crear_categoria()
            case '4':
                lista_total = mostrar_categorias(ruta)
                categoria_elegida = elegir_categoria(lista_total)
                eliminar_receta(categoria_elegida)
            case '5':
                eliminar_categoria()
            case '6':
                opcion = '6'


def mostrar_categorias(carpeta):
    print("Lista de categorias: ")
    ruta_categorias = Path(carpeta)
    print(ruta_categorias)
    lista_categorias = []
    contador = 1
    for archivo in ruta_categorias.iterdir():
        archivo_str = str(archivo.name)
        print(f'{contador} - {archivo_str}')
        lista_categorias.append(archivo)
        contador += 1
    return lista_categorias


def elegir_categoria(lista_armada):
    categoria = input('Seleccione una categoria\n')
    print(categoria)
    guia = Path('Recetas', categoria)

    if categoria == guia.name:
        guia = Path('Recetas', categoria)
        for numero, texto in enumerate(guia.glob('**/*.txt')):
            print(texto)
        return categoria


def elegir_receta(categoria):
    print(f'Usted escogió {categoria}')

    receta = input('¿Cuál receta desea ver?\n')
    return receta


def mostrar_recetas(receta, cat_receta):
    print(cat_receta)
    texto = '.txt'
    ruta_definitiva = receta + texto
    guia = Path('Recetas', cat_receta, ruta_definitiva)
    ruta_existe = guia.absolute()

    ruta_existente_windows = PureWindowsPath(ruta_existe)

    print(ruta_existe.read_text('utf-8'))
    desea_volver()


def desea_volver():
    volver = 'a'
    while volver.lower() != 'v':
        volver = input('¿Desea volver al inicio?, Presione \'v\'\n ')

    panel_de_opciones()


def crear_recetas(categoria):

    categoria2 = categoria.capitalize()

    nueva_receta = input("Escriba el nombre de la receta\n ")
    textos = input("escriba su receta\n")
    texto = '.txt'
    nueva_receta_unida = nueva_receta + texto

    carpeta = Path("C:\\Users\\lissm\\Documents\\Curso python udemy\\Dia 6\\Recetas")
    creando_receta = Path(carpeta, categoria2, Path(nueva_receta_unida))
    creando_receta.touch(exist_ok=True)
    creando_receta.write_text(textos)
    # creando_receta = Path(carpeta, categoria2, Path(nueva_receta_unida)).touch(exist_ok=True)

    # p = Path(nueva_receta_unida)
    # p.write_text(textos)

    desea_volver()


def crear_categoria():
    nueva_categoria = input("Escriba el nombre de la nueva categoria\n")
    carpeta = Path("C:\\Users\\lissm\\Documents\\Curso python udemy\\Dia 6\\Recetas")
    creando_categoria = Path(carpeta, Path(nueva_categoria)).mkdir(exist_ok=False)
    desea_volver()


def eliminar_receta(categoria):

    categoria2 = categoria.capitalize()

    receta_a_eliminar = input("Escriba el nombre de la receta que va a eliminar\n")
    texto = '.txt'
    receta_unida = receta_a_eliminar + texto
    carpeta = Path("C:\\Users\\lissm\\Documents\\Curso python udemy\\Dia 6\\Recetas")
    eliminando_receta = Path(carpeta, Path(categoria2, receta_unida)).unlink(missing_ok=False)
    print('se ha eliminado con éxito')
    limpiar_consola()
    desea_volver()


def eliminar_categoria():
    categoria = input("Escriba el nombre de la categoria que va a eliminar\n")
    carpeta = Path("C:\\Users\\lissm\\Documents\\Curso python udemy\\Dia 6\\Recetas")
    eliminando_categoria = Path(carpeta, Path(categoria)).rmdir()
    print('se ha eliminado con éxito')
    limpiar_consola()
    desea_volver()


def limpiar_consola():
    system('cls')


nombre = bienvenida()

contador_de_recetas()
panel_de_opciones()

