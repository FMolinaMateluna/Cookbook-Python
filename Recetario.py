import os
from pathlib import Path
from os import system

#Ruta relativa 
ruta_relativa = Path(Path.home(), 'Recetario Python','Recetas')

#Funcion para el conteo de recetas en el recetario
def conteo(ruta):
    contador = 0
    for recetas in Path(ruta).glob('**/*.txt'):
        contador +=1
    return contador
#Funcion para bienvenida
def bienvenida():
    nombre_usuario = input('Introduce tu nombre: ')
    return nombre_usuario
#Funcion para las opciones de la app
def menu(nombre):
    system('cls')
    print ('◠' * 55) 
    print (f' ¡¡ Bienvenido al programa de recetas de Florencia !! ')
    print ('◡' * 55)
    print('\n')
    print(f'》 {nombre} este recetario tiene {conteo(ruta_relativa)} recetas para que explores!  《')
    print('\n')
    eleccion_usuario = 'x'
    while not eleccion_usuario.isnumeric() or int(eleccion_usuario) not in range(1,7):
            print ('╍' * 40)
            print ('''MENU PRINCIPAL:
            [1] - LEER RECETA 
            [2] - NUEVA RECETA 
            [3] - NUEVA CATEGORIA 
            [4] - ELIMINAR RECETA 
            [5] - ELIMINAR CATEGORIA
            [6] - FINALIZAR''')
            print ('╍' * 40)
            print('\n')
            eleccion_usuario = input(' ➜ Elija una opcion: ')
            
    return int((eleccion_usuario))
'''Funciones para cada opcion que el usuario desee realizar, al final en un bucle while hacemos 
el llamado a cada una para que la app funcione correctamente'''
#Funcion para mostrar las categorias dentro del recetario
def mostrar_categorias (ruta):
    print('Categorias: ')
    ruta_categorias = Path(ruta)
    contador = 1
    lista_categorias = []
    for lista in ruta_categorias.iterdir():
        carpetas = str(lista.name)
        print(f'[{contador}] - [{carpetas}]')
        lista_categorias.append(lista)
        contador += 1
    
    return lista_categorias
#Funcion para elegir categorias
def elegir_categoria (lista):
    eleccion_usuario = 'x'

    while not eleccion_usuario.isnumeric() or int(eleccion_usuario) not in range(1, len(lista) + 1):
        eleccion_usuario = input('Elija una opcion: ')
    
    return lista[int(eleccion_usuario) - 1]
#Funcion para mostrar todas las recetas dentro de la categoria
def mostrar_recetas (ruta):
    print ('Recetas: ')
    ruta_recetas = Path(ruta)
    contador = 1
    lista_recetas = []
    for receta in ruta_recetas.glob('*.txt'):
        recetas = str(receta.name)
        print(f'[{contador}]-[{recetas}]')
        lista_recetas.append(receta)
        contador += 1
    
    return lista_recetas
#Funcion para elegir receta
def elegir_receta (lista):
    eleccion_receta = 'x'

    while not eleccion_receta.isnumeric() or int(eleccion_receta) not in range(1, len(lista) + 1):
        eleccion_receta = input('Elija una opcion: ')
    
    return lista[int(eleccion_receta) - 1]
#Funcion para leer receta
def leer_receta (receta):
    print(Path.read_text(receta))
#Funcion para escribir receta
def escribir_receta (ruta):
    existe = False

    while not existe:
        print ('Ingrese el nombre de su receta: ')
        nueva_receta = input() + '.txt'
        print ('Ingrese su receta nueva: ')
        nuevo_texto = input()
        ruta_nueva = Path(ruta, nueva_receta)

        if not os.path.exists(ruta_nueva):
            Path.write_text(ruta_nueva, nuevo_texto)
            print (f'Tu receta {nueva_receta} ha sido creada con exito!!')
            existe = True
        else:
            print ('Esta receta ya existe! Intenta con otra')
#Ingresar nueva categoria
def categoria_nueva (ruta): 
    existe = False

    while not existe:
        print ('Ingrese su nueva categoria: ')
        nueva_categoria = input()
        ruta_categoria = Path(ruta, nueva_categoria)

        if not os.path.exists(ruta_categoria):
            Path.mkdir(ruta_categoria)
            print (f'Tu categoria {nueva_categoria} ha sido creada con exito!!')
            existe = True
        
        else:
            print ('Esta categoria ya existe! Intenta con otra')
#Eliminar receta o categoria
def eliminar_receta (receta):
    print(Path.unlink(receta))
    print(f'La receta {receta.name} ha sido eliminada con exito! ')

def eliminar_categoria (categoria):
    Path(categoria).mkdir()
    print(f'La receta {categoria.name} ha sido eliminada con exito! ')
#Reinicio de menu
def inicio():
    opcion_salir = input('Volver al menu principal? SI/NO: ')
    finalizar = False

    if opcion_salir.lower() != 'si':
        print ('Programa finalizado! Gracias por su visita')
        finalizar = True
        return finalizar
    else:
        return finalizar
        

nombre = bienvenida()

finalizar = False

while not finalizar:
    menu_usuario = menu(nombre)
    if menu_usuario == 1:
        mis_categorias = mostrar_categorias(ruta_relativa)
        categoria_usuario = elegir_categoria(mis_categorias)
        mis_recetas = mostrar_categorias(categoria_usuario)
        if len(mis_recetas) < 1:
            print('Esta categoria no contiene ninguna receta!')
        else:
            receta_usuario = elegir_receta(mis_recetas)
            leer_receta(receta_usuario)
        finalizar = inicio()
    elif menu_usuario == 2:
        mis_categorias = mostrar_categorias(ruta_relativa)
        categoria_usuario = elegir_categoria(mis_categorias)
        escribir_receta (categoria_usuario)
        finalizar = inicio()
    elif menu_usuario == 3:
        mostrar_categorias(ruta_relativa)
        categoria_nueva (ruta_relativa)
        finalizar = inicio()
    elif menu_usuario == 4:
        mis_categorias = mostrar_categorias(ruta_relativa)
        categoria_usuario = elegir_categoria(mis_categorias)
        mis_recetas = mostrar_categorias(categoria_usuario)
        if len(mis_recetas) < 1: 
            print('Esta categoria no contiene ninguna receta!')
        else:
            receta_usuario = elegir_receta(mis_recetas)
            eliminar_receta(receta_usuario)
        finalizar = inicio()
    elif menu_usuario == 5:
        mis_categorias = mostrar_categorias(ruta_relativa)
        categoria_usuario = elegir_categoria(mis_categorias)
        eliminar_categoria(categoria_usuario)
        finalizar = inicio()
    elif menu_usuario == 6:
        print ('Programa finalizado! Gracias por su visita')
        finalizar = True


