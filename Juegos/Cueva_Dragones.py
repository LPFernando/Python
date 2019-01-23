#-*- coding: utf-8 -*

from random import randint
from time import sleep

def mostrar_Introduccion():
    print("Estas en una tierra llena de dragones. Frente a ti ")
    print("hay dos cuevas. En una de ellas, el dragón es generoso y amigable ")
    print("y compartir su tesoro contigo. El otro dragón ")
    print("es codicioso y esta hambriento, y te devorar� inmediatamente.")
    print(" ")

def elige_Cueva():
    cueva=""
    cueva=input("¿A qué cueva quieres entrar? (1 ó 2)")
    
    return cueva

def explorar_Cueva(cueva_Elegida):
    print("Te aproximas a la cueva...")
    sleep(2)
    print("Es oscura y espeluznante...")
    sleep(2)
    print("!Un gran dragon aparece súbitamente frente a ti! Abre sus fauces y ...")
    print()
    sleep(2)
    op_aleatoria=randint(1,2)
    
    if(op_aleatoria==int(cueva_Elegida)):
        print("¡Te regala su tesoro...!")
    else:
        print("¡Te engulle de un bocado!")

jugar_De_Nuevo="si"

while jugar_De_Nuevo=="si" or jugar_De_Nuevo=="s":
    mostrar_Introduccion()
    numero_cueva=elige_Cueva()
    explorar_Cueva(numero_cueva)
    
    print("¿Quieres jugar de nuevo? (si o no)")
    jugar_De_Nuevo=input()